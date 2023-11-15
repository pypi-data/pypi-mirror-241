import copy
from pathlib import Path
import torch
import torch.nn as nn
from torch.optim import Adam
from torchvision import transforms
from typing import List, Callable, Union, Dict
from tqdm import tqdm
from loguru import logger
import numpy as np
import sys

from sklearn.model_selection import train_test_split
import random
import mlflow
import mlflow.pytorch
import time
from sklearn.metrics import classification_report

sys.path.append("/home/alex/qi3/ml_dev_utils")

from mlutils.models.classifiers import PyTorchPrototypicalNetworkClassifier
from mlutils.models import ModelEnum
from mlutils.models.pytorch_model_last_layer_adaptor import AddLinearLayerAdaptor
from mlutils.dataimporters import PyTorchImagesDataSetWrapper
from mlutils.dataimporters import PyTorchTaskSampler
from mlutils.utils.file_utils import get_all_files, save_list_as_csv
from mlutils.utils.imgutils.image_transformers import to_rgb
from mlutils.utils.common_utils import set_seed
from mlutils.utils.plotutils import plot_avg_train_validate_accuracy, plot_avg_train_validate_loss


N_CLASSES = 2

# how many points to use in order to create
# the average point for a class
N_SUPPORT_POINTS =  5

# how many points to look into in order
# to establish the error
N_QUERY_POINTS =  10

# how many iterations to do over every
# batch
N_ITERATIONS = 20

N_WORKERS = 4

N_EPOCHS = 200

SEED = 42
LEARNING_RATE = 0.001
LR_SCHEDULER_STEP = 20
LR_SCHEDULER_GAMMA = 0.5
WEIGHT_DECAY = 0.05

IMG_SIZE = (256, 256)
MEAN = [0.4617, 0.4819, 0.4474]
STD = [0.2136, 0.2215, 0.2403]

IMG_TRAIN_PIPE = transforms.Compose([to_rgb,
                                     transforms.Resize(IMG_SIZE),
                                     transforms.ToTensor(),
                                     transforms.Normalize(MEAN, STD)])

TRAIN_IMAGES_PATH = Path("/home/alex/qi3/mir_datasets_new/cracks_v_3_id_8/train")
TEST_IMAGES_PATH = Path("/home/alex/qi3/mir_datasets_new/cracks_v_3_id_8/test")
EXPERIMENT_ID = "1"
EXPERIMENT_NAME = "crack_2_classes_proto_resnet18_base"
mlflow_track_uri_path = Path(f"/home/alex/qi3/ml_dev_utils/apps/mlruns")


def epoch_fit_model(model: PyTorchPrototypicalNetworkClassifier,
                    optimizer: torch.optim.Optimizer,
                    criterion: Callable,
                    data: torch.utils.data.DataLoader,
                    epoch_loss: List[float],
                    epoch_accuracy: List[float],
                    **kwargs):

    model.train()
    with tqdm(enumerate(data), total=len(data), desc="Training") as tqdm_train:
        for episode_index, (support_images, support_labels, query_images, query_labels, _,) in tqdm_train:

            if 'device' in kwargs:
                support_images = support_images.to(kwargs['device'])
                support_labels = support_labels.to(kwargs['device'])
                query_images = query_images.to(kwargs['device'])
                query_labels = query_labels.to(kwargs['device'])

            optimizer.zero_grad()

            # compute prototypes
            model.process_support_set(support_images, support_labels)

            # compute predictions
            outputs = model(query_images)
            loss = criterion(outputs, query_labels)
            loss.backward()
            optimizer.step()

            epoch_loss.append(loss.item())

            _, preds = torch.max(outputs, 1)

            n_preds = float(len(query_labels))
            ncorrect = torch.sum(preds == query_labels.data).item()
            epoch_accuracy.append(ncorrect / n_preds)

def epoch_validation_fit_model(model: PyTorchPrototypicalNetworkClassifier,
                               criterion: Callable,
                               data: torch.utils.data.DataLoader,
                               epoch_loss: List[float],
                               epoch_accuracy: List[float],
                               **kwargs):

    model.eval()
    validation_prototypes: List[torch.Tensor] = []
    with torch.no_grad():
        with tqdm(enumerate(data), total=len(data), desc="Validation") as tqdm_validate:
            for episode_index, (support_images, support_labels, query_images, query_labels, _,) in tqdm_validate:

                if 'device' in kwargs:
                    support_images = support_images.to(kwargs['device'])
                    support_labels = support_labels.to(kwargs['device'])
                    query_images = query_images.to(kwargs['device'])
                    query_labels = query_labels.to(kwargs['device'])

                # creates the prototypes this changes
                # the prototypes of the original model
                model.process_support_set(support_images, support_labels)
                validation_prototypes.append(model.prototypes)
                outputs = model(query_images)
                loss = criterion(outputs, query_labels)

                epoch_loss.append(loss.item())

                _, preds = torch.max(outputs, 1)
                n_preds = float(len(query_labels))
                ncorrect = torch.sum(preds == query_labels.data).item()
                epoch_accuracy.append(ncorrect / n_preds)

    epoch_average_prototypes = torch.mean(torch.stack(validation_prototypes), dim=0)
    return epoch_average_prototypes


def evaluate_on_one_task(model: PyTorchPrototypicalNetworkClassifier,
                         support_images: torch.Tensor, support_labels: torch.Tensor,
                         query_images: torch.Tensor, query_labels: torch.Tensor) -> [int, int]:
    """
    Returns the number of correct predictions of query labels, and the total number of predictions.
    """

    model.process_support_set(support_images, support_labels)
    model_outputs = model(query_images).detach().data
    max_preds_out = torch.max(model_outputs, 1)[1]
    max_preds = (max_preds_out == query_labels).sum().item()
    return max_preds, len(query_labels), max_preds_out, model.prototypes


def model_test(model: PyTorchPrototypicalNetworkClassifier,
               mlflow_run_id: str,
               prototypes_path: Path,
               **kwargs):

    logger.info(f"Starting model testing")
    time_start = time.time()

    if model is None:
        model_uri = f"runs:/{mlflow_run_id}/models"
        model_state = mlflow.pytorch.load_state_dict(model_uri, map_location=torch.device(device))

        model = PyTorchPrototypicalNetworkClassifier.load_with_state_dict(model_state=model_state,
                                                                              backbone_type=ModelEnum.RESNET_18,
                                                                              use_softmax=False,
                                                                              device=device,
                                                                              pretrained=True,
                                                                              freeze_model_params=True,
                                                                              weights=None,
                                                                              model_adaptor=AddLinearLayerAdaptor(
                                                                                  params={"out": "LAST_LAYER"})).to(device)

        prototypes = torch.load(prototypes_path, map_location=torch.device(device))
        model.prototypes = prototypes

    model.eval()

    test_corrosion_images = get_all_files(dir_path=TEST_IMAGES_PATH / "cracked",
                                          file_formats=[".png", ".jpg", ".jpeg"],
                                          skip_dirs=False)

    logger.info(f"Found {len(test_corrosion_images)} corrosion test images")

    test_no_corrosion_images = get_all_files(dir_path=TEST_IMAGES_PATH / "uncracked",
                                             file_formats=[".png", ".jpg", ".jpeg"],
                                             skip_dirs=False)

    logger.info(f"Found {len(test_no_corrosion_images)}  uncracked test images")

    images_paths = test_corrosion_images + test_no_corrosion_images
    labels = [1] * len(test_corrosion_images) + [0] * len(test_no_corrosion_images)

    # shuffle images and labels
    new_total = []
    for img, label in zip(images_paths, labels):
        new_total.append((img, label))

    random.shuffle(new_total)

    for i, item in enumerate(new_total):
        images_paths[i] = item[0]
        labels[i] = item[1]

    test_dataset = PyTorchImagesDataSetWrapper.from_file_sources(filenames=images_paths,
                                                                 labels=labels,
                                                                 on_load_transformers=IMG_TRAIN_PIPE)

    logger.info(f"Size of test dataset {len(test_dataset)}")

    labels = test_dataset.get_labels()
    predictions = []
    with torch.no_grad():

        for x, y in test_dataset:

            x = x.to(device)
            # could use x.unsqueeze(0) here also
            model_outputs = model(torch.stack([x])).detach().data
            max_preds_out = torch.max(model_outputs, 1)[1]
            max_preds_out = max_preds_out.cpu()
            predictions.append(max_preds_out.item())


    # classification report from sklearn will produce something
    # like the following
    # {'No Corrosion': {'precision': 0.6459627329192547, 'recall': 0.8482871125611745, 'f1-score': 0.7334273624823695, 'support': 613},
    #  'Corrosion': {'precision': 0.8374125874125874, 'recall': 0.6269633507853403, 'f1-score': 0.7170658682634728, 'support': 764},
    #  'accuracy': 0.7254901960784313,
    #  'macro avg': {'precision': 0.741687660165921, 'recall': 0.7376252316732574, 'f1-score': 0.7252466153729211, 'support': 1377},
    #  'weighted avg': {'precision': 0.7521847291668263, 'recall': 0.7254901960784313, 'f1-score': 0.724349525457506, 'support': 1377}}
    report = classification_report(y_true=labels, y_pred=predictions,
                                   target_names=["No Crack", "Crack"],
                                   output_dict=True)

    logger.info(f"Classfication report {report}")

    metrics_to_log = {'no_crack_test_precision': report['No Crack']['precision'],
                      'no_crack_test_recall': report['No Crack']['recall'],
                      'no_crack_test_f1_score': report['No Crack']['f1-score'],
                      'no_crack_test_support': report['No Crack']['support'],
                      'crack_test_precision': report['Crack']['precision'],
                      'crack_test_recall': report['Crack']['recall'],
                      'crack_test_f1_score': report['Crack']['f1-score'],
                      'crack_test_support': report['Crack']['support'],
                      'accuracy_test': report['accuracy'],
                      'test_macro_avg_precision': report['macro avg']['precision'],
                      'test_macro_avg_recall': report['macro avg']['recall'],
                      'test_macro_avg_f1_score': report['macro avg']['f1-score'],
                      'test_macro_avg_support': report['macro avg']['support'],
                      'test_weighted_avg_precision': report['weighted avg']['precision'],
                      'test_weighted_avg_recall': report['weighted avg']['recall'],
                      'test_weighted_avg_f1_score': report['weighted avg']['f1-score'],
                      'test_weighted_avg_support': report['weighted avg']['support'],
    }

    mlflow.log_metrics(metrics_to_log)
    time_end = time.time()
    logger.info(f"Total testing time {time_end - time_start}")


def model_train(model: PyTorchPrototypicalNetworkClassifier, train_data, val_data):

    logger.info(f"Starting model training")
    time_start = time.time()

    # we are training the model
    model.train()

    # loss function to use
    loss = nn.CrossEntropyLoss()

    # create an optimzer
    params_to_update = model.parameters()

    optimizer = Adam(params_to_update,
                     lr=LEARNING_RATE,
                     weight_decay=WEIGHT_DECAY)

    # scheduler to adapt the learning rate
    # for more information check https://pytorch.org/docs/stable/optim.html
    lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer=optimizer,
                                                   gamma=LR_SCHEDULER_GAMMA,
                                                   step_size=LR_SCHEDULER_STEP)

    # monitor loss and accuracy
    total_train_accuracy = []
    total_train_loss = []
    total_validation_accuracy = []
    total_validation_loss = []

    val_loss = nn.CrossEntropyLoss()

    logger.info(f"Starting learning rate {lr_scheduler.get_last_lr()}")

    # let mlflow know that we are starting a run
    with mlflow.start_run(run_name=EXPERIMENT_NAME,
                          experiment_id=EXPERIMENT_ID) as mlflow_run:

        artifact_uri = mlflow_run.info.artifact_uri

        logger.info(f"MLFlow artifact URI {artifact_uri}")

        mlflow_run_id = mlflow.active_run().info.run_id

        # for that run we want to log various parameters
        mlflow.log_param("DATASET_NAME", "corrosion_v_3_id_9")
        mlflow.log_param("N_CLASSES", N_CLASSES)
        mlflow.log_param("N_ITERATIONS", N_ITERATIONS)
        mlflow.log_param("N_EPOCHS", N_EPOCHS)
        mlflow.log_param("LR Scheduler", "StepLR")
        mlflow.log_param("LR_SCHEDULER_GAMMA", LR_SCHEDULER_GAMMA)
        mlflow.log_param("LR_SCHEDULER_STEP", LR_SCHEDULER_STEP)
        mlflow.log_param("N_SUPPORT_POINTS", N_SUPPORT_POINTS)
        mlflow.log_param("N_QUERY_POINTS", N_QUERY_POINTS)
        mlflow.log_param("SEED", SEED)
        mlflow.log_param("WEIGHT_DECAY", WEIGHT_DECAY)
        mlflow.log_param("N_QUERY_POINTS", N_QUERY_POINTS)
        mlflow.log_param("NORMALIZATION_IMAGE_MEAN", MEAN)
        mlflow.log_param("NORMALIZATION_IMAGE_STD", STD)

        best_validation_accuracy = float("-inf")
        best_model_state: Dict = None
        best_average_validation_prototypes: torch.Tensor = None

        for epoch in range(N_EPOCHS):
            logger.info("=====================================================")
            logger.info(
                f"On training epoch {epoch}/{N_EPOCHS} ({float(epoch) / float(N_EPOCHS) * 100.0}%)")
            logger.info(f"Learning rate {lr_scheduler.get_last_lr()}")

            mlflow.log_metric("lr", lr_scheduler.get_last_lr()[0])

            epoch_train_loss = []
            epoch_train_accuracy = []
            epoch_fit_model(model=model, criterion=loss,
                            optimizer=optimizer, data=train_data,
                            epoch_accuracy=epoch_train_accuracy,
                            epoch_loss=epoch_train_loss,
                            device=device)

            logger.info(f"Epoch train average loss {np.mean(epoch_train_loss)}")
            logger.info(f"Epoch train average accuracy {np.mean(epoch_train_accuracy)}")
            total_train_accuracy.append(np.mean(epoch_train_accuracy))
            total_train_loss.append(np.mean(epoch_train_loss))
            mlflow.log_metric("average_train_accuracy", np.mean(epoch_train_accuracy), step=epoch)
            mlflow.log_metric("average_train_loss", np.mean(epoch_train_loss), step=epoch)

            epoch_validation_loss = []
            epoch_validation_accuracy = []
            average_validation_prototypes = epoch_validation_fit_model(model=model, criterion=val_loss,
                                                                       epoch_accuracy=epoch_validation_accuracy,
                                                                       epoch_loss=epoch_validation_loss,
                                                                       data=val_data, device=device)

            mean_epoch_accuracy = np.mean(epoch_validation_accuracy)

            if mean_epoch_accuracy > best_validation_accuracy:
                best_validation_accuracy = mean_epoch_accuracy
                best_model_state = model.state_dict()
                best_average_validation_prototypes = copy.deepcopy(average_validation_prototypes)

            logger.info(f"Epoch validation average loss {np.mean(epoch_validation_loss)}")
            logger.info(f"Epoch validation average accuracy {np.mean(epoch_validation_accuracy)}")
            logger.info(f"Epoch validation best accuracy {best_validation_accuracy}")
            total_validation_accuracy.append(np.mean(epoch_validation_accuracy))
            total_validation_loss.append(np.mean(epoch_validation_loss))

            mlflow.log_metric("average_validation_accuracy", np.mean(epoch_validation_accuracy), step=epoch)
            mlflow.log_metric("average_validation_loss", np.mean(epoch_validation_loss), step=epoch)
            mlflow.log_metric("best_validation_accuracy", best_validation_accuracy, step=epoch)

            # make a step of the scheduler that controls the
            # learning rate
            lr_scheduler.step()

        logger.info(f"Logging best model state at URI: {artifact_uri}/models")

        # save the best model
        model_uri = f"models"
        mlflow.pytorch.log_state_dict(best_model_state, model_uri)

        mlflow_run_path = mlflow_track_uri_path / str(EXPERIMENT_ID)
        prototypes_path =  mlflow_run_path / f"{mlflow_run_id}/artifacts/models/best_average_validation_prototypes.pth"
        torch.save(best_average_validation_prototypes, prototypes_path)

        time_end = time.time()
        logger.info(f"Total training time {time_end - time_start}")


        plot_avg_train_validate_loss(n_epochs=N_EPOCHS,
                                     train_loss=total_train_loss,
                                     validate_loss=total_validation_loss,
                                     use_mean_smoothing=True,
                                     step_length=20,
                                     save_file=mlflow_run_path / f"{mlflow_run_id}/artifacts/loss.png",
                                     show_before_save=False)

        save_list_as_csv(list_inst=total_train_loss,
                         filename= mlflow_run_path / f"{mlflow_run_id}/artifacts/train_loss.csv",
                         write_default_header = True,
                         header= None)

        save_list_as_csv(list_inst=total_validation_loss,
                         filename=  mlflow_run_path / f"{mlflow_run_id}/artifacts/validate_loss.csv",
                         write_default_header=True,
                         header=None)
        #
        plot_avg_train_validate_accuracy(n_epochs=N_EPOCHS,
                                         train_accuracy=total_train_accuracy,
                                         validate_accuracy=total_validation_accuracy,
                                         use_mean_smoothing=True,
                                         step_length=20,
                                         save_file= mlflow_run_path / f"{mlflow_run_id}/artifacts/accuracy.png",
                                         show_before_save=False)
        #
        save_list_as_csv(list_inst=total_train_accuracy,
                         filename= mlflow_run_path /f"{mlflow_run_id}/artifacts/train_accuracy.csv",
                         write_default_header=True,
                         header=None)

        save_list_as_csv(list_inst=total_validation_accuracy,
                         filename=mlflow_run_path / f"{mlflow_run_id}/artifacts/validate_accuracy.csv",
                         write_default_header=True,
                         header=None)

        model_test(model=None, mlflow_run_id=mlflow_run_id,
                   prototypes_path=prototypes_path, device=device)

    mlflow.end_run()
    return mlflow_run_id


if __name__ == '__main__':


    mlflow.set_tracking_uri(mlflow_track_uri_path)
    mlflow.create_experiment(EXPERIMENT_ID)
    logger.info(mlflow.get_tracking_uri())
    logger.info(mlflow.get_registry_uri())

    # se the seed for any random
    # operations that come latter or
    set_seed(SEED)

    if torch.cuda.is_available():
        logger.info("CUDA is available")
        logger.info(f"Number of devices found: {torch.cuda.device_count()}")
        logger.info(f"Device name {torch.cuda.get_device_name(0)}")

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    train_cracked_images = get_all_files(dir_path=TRAIN_IMAGES_PATH / "cracked",
                                           file_formats=[".png", ".jpg", ".jpeg"],
                                           skip_dirs=False)

    logger.info(f"Found {len(train_cracked_images)} train cracked images")

    train_no_cracked_images = get_all_files(dir_path=TRAIN_IMAGES_PATH / "uncracked",
                                           file_formats=[".png", ".jpg", ".jpeg"],
                                           skip_dirs=False)

    logger.info(f"Found {len(train_no_cracked_images)} no crack train images")

    images_paths = train_cracked_images + train_no_cracked_images
    labels = [1] * len(train_cracked_images) + [0] * len(train_no_cracked_images)

    # shuffle images and labels
    total = []
    for img, label in zip(images_paths, labels):
        total.append((img, label))

    random.shuffle(total)

    for i, item in enumerate(total):
        images_paths[i] = item[0]
        labels[i] = item[1]


    x_train, x_validate, y_train, y_validate = train_test_split(images_paths,
                                                                labels,
                                                                test_size=0.2,
                                                                random_state=SEED,
                                                                shuffle=True)

    train_dataset = PyTorchImagesDataSetWrapper.from_file_sources(filenames=x_train,
                                                                  labels=y_train,
                                                                  on_load_transformers=IMG_TRAIN_PIPE)

    logger.info(f"Size of train dataset {len(train_dataset)}")


    batch_sampler = PyTorchTaskSampler(dataset=train_dataset,
                                       n_way=N_CLASSES,
                                       n_shot=N_SUPPORT_POINTS, n_query=N_QUERY_POINTS,
                                       n_tasks=N_ITERATIONS)

    train_data_loader = torch.utils.data.DataLoader(train_dataset,
                                              batch_sampler=batch_sampler,
                                              num_workers=N_WORKERS,
                                              pin_memory=True,
                                              collate_fn=batch_sampler.episodic_collate_fn)

    val_dataset = PyTorchImagesDataSetWrapper.from_file_sources(filenames=x_validate,
                                                                labels=y_validate,
                                                                on_load_transformers=IMG_TRAIN_PIPE)

    logger.info(f"Size of validation dataset {len(val_dataset)}")

    batch_sampler = PyTorchTaskSampler(dataset=val_dataset,
                                       n_way=N_CLASSES,
                                       n_shot=N_SUPPORT_POINTS, n_query=N_QUERY_POINTS,
                                       n_tasks=N_ITERATIONS)

    val_data_loader = torch.utils.data.DataLoader(val_dataset,
                                              batch_sampler=batch_sampler,
                                              num_workers=N_WORKERS,
                                              pin_memory=True,
                                              collate_fn=batch_sampler.episodic_collate_fn)

    model = PyTorchPrototypicalNetworkClassifier.build(
        #model_path=Path("/home/alex/qi3/mir_models/corrosion_protonet_resnet18_model.pth"),
        device=device,
        weights=None,
        pretrained=True,
        freeze_model_params=True,
        use_softmax=False,
        backbone_type=ModelEnum.RESNET_18,
        model_adaptor=AddLinearLayerAdaptor(params={"out": "LAST_LAYER"}))

    mlflow_run_id = model_train(model=model, train_data=train_data_loader, val_data=val_data_loader)