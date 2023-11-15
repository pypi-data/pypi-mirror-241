"""module pytorch_data_set.
Wrapper for representing a datasets set
when using PyTorch models

"""

from typing import List, Any, Callable
from pathlib import Path
import torch
import torch.utils.data as data
import numpy as np

from mlutils.utils.imgutils.image_io import load_img
from mlutils.utils.mode_enum import ModeEnum
from mlutils.utils.exceptions import SizeMismatchException


class PyTorchImagesDataSetWrapper(data.Dataset):

    @classmethod
    def from_file_sources(cls, filenames: List[Path], labels: List[int],
                          mode: ModeEnum = ModeEnum.TRAIN,
                          image_loader: Callable = load_img,
                          on_load_transformers: Callable = None) -> "PyTorchImagesDataSetWrapper":
        """Build the image dataset from the given filenames and the specified
        labels

        Parameters
        ----------
        filenames: The files names to load the dataset
        labels: The labels of the images. This should be aligned with the filenames
        mode: The mode of the dataset
        image_loader: The callable that laods an image
        on_load_transformers: The transformation to use when loading an image

        Returns
        -------
        An instance of ImagesDataset
        """

        if len(filenames) != len(labels):
            raise SizeMismatchException(size1=len(filenames), size2=len(labels))

        # get the unique labels
        unique_labels = np.unique(labels)

        # build an empty dataset
        dataset = PyTorchImagesDataSetWrapper(mode=mode, unique_labels=list(unique_labels))

        # populate the labels
        dataset.y = labels

        # actually load the images
        dataset.data = [image_loader(img_path, on_load_transformers) for img_path in filenames]

        return dataset

    @classmethod
    def from_images_and_labels(cls, x: torch.Tensor, y: torch.Tensor,
                               mode: ModeEnum = ModeEnum.TRAIN) -> "PyTorchImagesDataSetWrapper":
        """Load the dataset from the given Tensor of image data
        and the labels corresponding to the images

        Parameters
        ----------
        x: The Tensor that holds the images data
        y: The Tensor that holds the labels
        mode: The mode of the dataset

        Returns
        -------

        An instance of ImagesDataset
        """

        unique_labels = np.unique(y)

        # build an empty dataset
        dataset = PyTorchImagesDataSetWrapper(mode=mode, unique_labels=list(unique_labels),
                                              transform=None, target_transform=None)

        # populate the labels
        dataset.y = y

        # actually load the images
        dataset.data = x

        return dataset

    def __init__(self, mode: ModeEnum, unique_labels: List[Any],
                 transform: Callable = None, target_transform: Callable = None):
        super(PyTorchImagesDataSetWrapper, self).__init__()
        self.mode = mode

        self.unique_labels: List[Any] = unique_labels
        self.transform: Callable = transform
        self.target_transform: Callable = target_transform
        self.y: List[int] = []
        self.data: List[Any] = []

    @property
    def n_classes(self) -> int:
        return len(self.unique_labels)

    def get_labels(self) -> List[int]:
        """ Returns the labels list

        Returns
        -------
        """
        return self.y

    def __getitem__(self, idx: int) -> tuple:
        """Returns the idx-th datasets point
        in the datasets set

        Parameters
        ----------
        idx: The index of the data to request

        Returns
        -------
        """

        x = self.data[idx]
        if self.transform:
            x = self.transform(x)

        y = self.y[idx]
        if self.target_transform:
            y = self.target_transform(y)

        return x, y

    def __len__(self):
        """Returns the size of the datasets set

        Returns
        -------

        """
        if self.data is None:
            return 0
        return len(self.data)
