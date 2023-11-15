import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import time
import PIL
from PIL.Image import Image as PILImage
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, mean_squared_error

from mlutils.utils import load_images
from mlutils.utils import ImageLoadersEnumType

IMAGES_PATH = Path('/home/alex/qi3/mir_datasets_new/corrosion_v_3_id_9')
TRAIN_CORROSION_IMGS_PATH = IMAGES_PATH / "train/corrosion"
TRAIN_NO_CORROSION_IMGS_PATH = IMAGES_PATH / "train/no_corrosion"

TEST_CORROSION_IMGS_PATH = IMAGES_PATH / "test/corrosion"
TEST_NO_CORROSION_IMGS_PATH = IMAGES_PATH / "test/no_corrosion"

IMG_SIZE = (256, 256)

def resize_image(image: PILImage):
    return image.resize(size=IMG_SIZE)


def advanced_grid_search(x_train, y_train, x_test, y_test, ml_pipeline, params, cv=3, include_probas=False,
                         is_regression=False):
    '''
    This helper function will grid search a machine learning pipeline with feature engineering included
    and print out a classification report for the best param set.
    Best here is defined as having the best cross-validated accuracy on the training set
    '''

    model_grid_search = GridSearchCV(ml_pipeline, param_grid=params, cv=cv, error_score=-1)
    start_time = time.time()  # capture the start time

    model_grid_search.fit(x_train, y_train)

    best_model = model_grid_search.best_estimator_

    y_preds = best_model.predict(x_test)

    if is_regression:
        rmse = np.sqrt(mean_squared_error(y_pred=y_preds, y_true=test_set['pct_change_eod']))
        print(f'RMSE: {rmse:.5f}')
    else:
        print(classification_report(y_true=y_test, y_pred=y_preds))
    print(f'Best params: {model_grid_search.best_params_}')
    end_time = time.time()
    print(f"Overall took {(end_time - start_time):.2f} seconds")

    if include_probas:
        y_probas = best_model.predict_proba(x_test).max(axis=1)
        return best_model, y_preds, y_probas

    return best_model, y_preds

def load_train_set():
    corrosion_images = load_images(path=TRAIN_CORROSION_IMGS_PATH,
                                   loader=ImageLoadersEnumType.PIL_NUMPY,
                                   transformer=resize_image
                                   )
    no_corrosion_images = load_images(path=TRAIN_NO_CORROSION_IMGS_PATH,
                                      loader=ImageLoadersEnumType.PIL_NUMPY,
                                      transformer=resize_image
                                      )

    print(f"Number of corrosion images {len(corrosion_images)}")
    print(f"Number of no_corrosion images {len(no_corrosion_images)}")

    # let's stack the images together
    images = np.vstack(corrosion_images + no_corrosion_images)
    labels = [1] * len(corrosion_images) + [0] * len(no_corrosion_images)

    # calculate means
    avg_training_images = images.mean(axis=2).reshape(len(corrosion_images) + len(no_corrosion_images), -1)
    return avg_training_images, labels

def load_test_set():
    corrosion_images = load_images(path=TEST_CORROSION_IMGS_PATH,
                                   loader=ImageLoadersEnumType.PIL_NUMPY,
                                   transformer=resize_image
                                   )
    no_corrosion_images = load_images(path=TEST_NO_CORROSION_IMGS_PATH,
                                      loader=ImageLoadersEnumType.PIL_NUMPY,
                                      transformer=resize_image
                                      )

    print(f"Number of corrosion images {len(corrosion_images)}")
    print(f"Number of no_corrosion images {len(no_corrosion_images)}")

    # let's stack the images together
    images = np.vstack(corrosion_images + no_corrosion_images)
    labels = [1] * len(corrosion_images) + [0] * len(no_corrosion_images)

    # calculate means
    avg_test_images = images.mean(axis=2).reshape(len(corrosion_images) + len(no_corrosion_images), -1)
    return avg_test_images, labels

if __name__ == '__main__':

    avg_training_images, train_labels = load_train_set()
    print(f"Shape of average training images {avg_training_images.shape}")

    avg_test_images, test_labels = load_test_set()
    print(f"Shape of average training images {avg_test_images.shape}")
    # train baseline model using average pixel values


    clf = LogisticRegression(max_iter=100,
                             n_jobs=4,
                             solver='saga')

    ml_pipeline = Pipeline([
        ('classifier', clf)
    ])

    params = {  # C
        'classifier__C': [1e-1, 1e0, 1e1]
    }

    print("Average Pixel Value + LogReg\n==========================")
    advanced_grid_search(
        x_train=avg_training_images,
        y_train=train_labels,
        x_test=avg_test_images,
        y_test=test_labels,
        ml_pipeline=ml_pipeline,
        params=params
    )
