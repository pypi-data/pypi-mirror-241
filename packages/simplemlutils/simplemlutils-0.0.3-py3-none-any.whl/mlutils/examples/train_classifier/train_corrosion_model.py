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
import matplotlib.pyplot as plt
import csv
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
from mlutils.utils.file_utils import get_all_files, save_list_as_csv
from mlutils.dataimporters import PyTorchTaskSampler
from mlutils.utils.imgutils.image_transformers import to_rgb
from mlutils.utils.common_utils import set_seed

N_CLASSES = 2

# how many points to use in order to create
# the average point for a class
N_SUPPORT_POINTS = 1 # 5

# how many points to look into in order
# to establish the error
N_QUERY_POINTS = 1 # 10

# how many iterations to do over every
# batch
N_ITERATIONS = 20

N_WORKERS = 4

N_EPOCHS = 2

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

TRAIN_IMAGES_PATH = Path("/home/alex/qi3/mir_datasets_new/corrosion_v_3_id_9/train")
TEST_IMAGES_PATH = Path("/home/alex/qi3/mir_datasets_new/corrosion_v_3_id_9/test")
EXPERIMENT_ID = "1"
EXPERIMENT_NAME = "corrosion_2_classes_proto_resnet18_base"
mlflow_track_uri_path = Path(f"/home/alex/qi3/ml_dev_utils/mlutils/examples/train_classifier/mlruns")

def load_list_from_csv(filename: Path) -> List[float]:
    """Loads a list form the given csv file

    Parameters
    ----------
    filename

    Returns
    -------

    A list of floats
    """
    with open(filename, 'r') as fh:
        reader = csv.reader(fh, delimiter=",")

        data: List[float] = []

        for item in reader:

            if not item:
                continue
            else:
                data.append(float((item[1])))
        return data


def _add_plot(n_epochs: int, data: Union[Path, List[float]],
              label: str,
              step_length: int = 100,
              use_mean_smoothing: bool = True):

    if isinstance(data, Path):
        data = load_list_from_csv(filename=data)
    data_avg = np.empty(n_epochs)

    if use_mean_smoothing:
        for t in range(n_epochs):
            data_avg[t] = np.mean(data[max(0, t - step_length): (t + 1)])

        plt.plot(data_avg, label=label)
    else:
        plt.plot(data, label=label)

def plot_avg_train_validate_loss(n_epochs,
                                 train_loss: Union[Path, List[float]], step_length: int =100,
                                 validate_loss: Union[Path, List[float]]=None,
                                 use_mean_smoothing: bool = True,
                                 save_file: Path = None,
                                 title: str = None,
                                 show_before_save: bool = False):
    # load training loss and accuracy

    if train_loss is not None:
        _add_plot(n_epochs=n_epochs, data=train_loss,
                  step_length=step_length, label="Train loss",
                  use_mean_smoothing=use_mean_smoothing)

    if validate_loss is not None:
        _add_plot(n_epochs=n_epochs, data=validate_loss, step_length=step_length,
                  label="Validate loss", use_mean_smoothing=use_mean_smoothing)

    plt.xlabel("Epoch" if use_mean_smoothing else "Iteration")
    plt.ylabel("Loss")
    if validate_loss is not None and train_loss is not None:

        if title is None:
            plt.title("Average train/validate loss over epochs")
        else:
            plt.title(title)
    elif train_loss is not None:

        plt.title("Average train loss over epochs")

        if title is not None:
            plt.title(title)

    elif validate_loss is not None:
        plt.title("Average validate loss over epochs")

        if title is not None:
            plt.title(title)
    else:
        raise ValueError("No file path is specified")

    plt.legend(loc='best')
    plt.grid(True)

    if save_file is not None:

        if show_before_save:
            plt.show()

        plt.savefig(str(save_file))

        # need to close the figure
        # otherwise it may be overriden
        plt.close()
    else:
        plt.show()

def plot_avg_train_validate_accuracy(n_epochs: int,
                                     train_accuracy: Union[Path, List[float]],
                                     step_length: int = 100,
                                     validate_accuracy: Union[Path, List[float]]=None,
                                     use_mean_smoothing: bool = True,
                                     save_file: Path = None,
                                     title: str = None,
                                     show_before_save: bool = False):

    if train_accuracy is not None:
        _add_plot(n_epochs=n_epochs, data=train_accuracy,
                  step_length=step_length, label="Train accuracy",
                  use_mean_smoothing=use_mean_smoothing)

    if validate_accuracy is not None:
        _add_plot(n_epochs=n_epochs, data=validate_accuracy,
                  step_length=step_length, label="Validate accuracy",
                  use_mean_smoothing=use_mean_smoothing)

    plt.xlabel("Epoch" if use_mean_smoothing else "Iteration")
    plt.ylabel("Accuracy")
    if validate_accuracy is not None:
        plt.title("Average train/validate accuracy over epochs")
    else:
        plt.title("Average train accuracy over epochs")

    if title is not None:
        plt.title(title)

    plt.legend(loc='best')
    plt.grid(True)

    if save_file is not None:

        if show_before_save:
            plt.show()

        plt.savefig(str(save_file))

        # need to close the figure
        # otherwise it may be overriden
        plt.close()
    else:
        plt.show()


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

    test_corrosion_images = get_all_files(dir_path=TEST_IMAGES_PATH / "corrosion",
                                          file_formats=[".png", ".jpg", ".jpeg"],
                                          skip_dirs=False)

    logger.info(f"Found {len(test_corrosion_images)} corrosion test images")

    test_no_corrosion_images = get_all_files(dir_path=TEST_IMAGES_PATH / "no_corrosion",
                                             file_formats=[".png", ".jpg", ".jpeg"],
                                             skip_dirs=False)

    logger.info(f"Found {len(test_no_corrosion_images)} no corrosion test images")

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
                                   target_names=["No Corrosion", "Corrosion"],
                                   output_dict=True)

    logger.info(f"Classfication report {report}")

    metrics_to_log = {'no_corrosion_test_precision': report['No Corrosion']['precision'],
                      'no_corrosion_test_recall': report['No Corrosion']['recall'],
                      'no_corrosion_test_f1_score': report['No Corrosion']['f1-score'],
                      'no_corrosion_test_support': report['No Corrosion']['support'],
                      'corrosion_test_precision': report['Corrosion']['precision'],
                      'corrosion_test_recall': report['Corrosion']['recall'],
                      'corrosion_test_f1_score': report['Corrosion']['f1-score'],
                      'corrosion_test_support': report['Corrosion']['support'],
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


    # batch_sampler = PyTorchTaskSampler(dataset=test_dataset,
    #                                        n_way=N_CLASSES,
    #                                        n_shot=N_SUPPORT_POINTS, n_query=N_QUERY_POINTS,
    #                                        n_tasks=N_ITERATIONS)
    #
    # test_data_loader = torch.utils.data.DataLoader(test_dataset,
    #                                                    batch_sampler=batch_sampler,
    #                                                    num_workers=N_WORKERS,
    #                                                    pin_memory=True,
    #                                                    collate_fn=batch_sampler.episodic_collate_fn)
    #
    # total_predictions = 0
    # correct_predictions = 0
    #
    # model.eval()
    # best_accuracy_on_test = 0
    # with torch.no_grad():
    #     for episode_index, (support_images, support_labels, query_images, query_labels, class_ids) in \
    #                 tqdm(enumerate(test_data_loader), total=len(test_data_loader), desc="Testing"):
    #
    #         if 'device' in kwargs:
    #             support_images = support_images.to(kwargs['device'])
    #             support_labels = support_labels.to(kwargs['device'])
    #             query_images = query_images.to(kwargs['device'])
    #             query_labels = query_labels.to(kwargs['device'])
    #
    #         correct, total, model_outputs, prototypes = evaluate_on_one_task(model=model,
    #                                                                          support_images=support_images,
    #                                                                          support_labels=support_labels,
    #                                                                          query_images=query_images,
    #                                                                          query_labels=query_labels)
    #         error_class_0 = 0
    #         error_class_1 = 1
    #
    #         for i, label in enumerate(query_labels):
    #                 ground_truth = label
    #                 predicted = model_outputs[i].item()
    #
    #                 if ground_truth == 0 and predicted == 1:
    #                     error_class_0 += 1
    #                 elif ground_truth == 1 and predicted == 0:
    #                     error_class_1 += 1
    #
    #         task_accuracy = float(correct) / float(total)
    #
    #         if task_accuracy > best_accuracy_on_test:
    #                 best_accuracy_on_test = task_accuracy
    #             #     torch.save(prototypes, app_config.config.TEST_PROTOTYPES_PATH)
    #
    #         logger.info(f"\n")
    #         logger.info(f"On test task {episode_index}  class_0 images incorrect {error_class_0}")
    #         logger.info(f"On test task {episode_index}  class_1 images incorrect {error_class_1}")
    #
    #         total_predictions += total
    #         correct_predictions += correct
    #
    # test_accuracy = (100 * correct_predictions / total_predictions)
    # logger.info(f"Model tested on {len(test_data_loader)} tasks. "
    #                 f"Accuracy: {test_accuracy:.2f}%")
    # mlflow.log_metric("test_accuracy", test_accuracy)
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
        best_model_filename = f"best_protonet_resnet18_corrosion_{mlflow_run_id}.pth"

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

    train_corrosion_images = get_all_files(dir_path=TRAIN_IMAGES_PATH / "corrosion",
                                           file_formats=[".png", ".jpg", ".jpeg"],
                                           skip_dirs=False)[0: 10]

    logger.info(f"Found {len(train_corrosion_images)} train images")

    train_no_corrosion_images = get_all_files(dir_path=TRAIN_IMAGES_PATH / "no_corrosion",
                                           file_formats=[".png", ".jpg", ".jpeg"],
                                           skip_dirs=False)[0: 10]

    logger.info(f"Found {len(train_no_corrosion_images)} no train images")

    images_paths = train_corrosion_images + train_no_corrosion_images
    labels = [1] * len(train_corrosion_images) + [0] * len(train_no_corrosion_images)

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