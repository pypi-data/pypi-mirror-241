from pathlib import Path
import matplotlib.pyplot as plt
from typing import List, Callable, Union, Dict
import numpy as np

from mlutils.utils.file_utils import load_list_from_csv


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
