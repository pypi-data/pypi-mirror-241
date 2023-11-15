"""module img_transformers. Various utilities
for transforming images

"""
import enum
from typing import Callable, List, TypeVar
from pathlib import Path

import numpy
import numpy as np
from PIL import Image
from PIL import ImageOps
import torchvision.transforms as transforms
import torch

from mlutils.utils.imgutils.image_enums import ImageLoadersEnumType
from mlutils.utils.imgutils.image_io import load_img, ImageWriters

ImageType = TypeVar("ImageType")

class ImageAugmentType(enum.Enum):
    INVALID = 0
    RANDOM_CROP = 1
    COLOR_JITTER = 2


class ImageTransformerWrapper(object):
    def __init__(self, transform_op: Callable, *args):
        self.transform_op = transform_op
        self.args = args

    def __call__(self, img: Image):
        if self.args is not None and len(self.args) != 0 and self.args[0] is not None:
            return self.transform_op(img, *self.args)
        else:
            return self.transform_op(img)


def to_pytorch_tensor(img: Image, unsqueeze_dim: int = 0) -> torch.Tensor:
    """Converts the PIL.Image item into a torch.Tensor

    Parameters
    ----------
    img: The PIL.Image to convert
    unsqueeze_dim: The dimension to unsqueeze the produced torch tensor

    Returns
    -------

    An instance of torch.Tensor
    """

    if unsqueeze_dim is None or unsqueeze_dim == -1:
        return transforms.ToTensor()(img)
    else:
        return transforms.ToTensor()(img).unsqueeze_(unsqueeze_dim)


def pytorch_tensor_to_numpy(img: torch.Tensor):
    return img.cpu().detach().numpy()


def pil_image_from_array(img: List):
    return Image.fromarray(np.uint8(img))


def resize_image(img: Image, size: tuple) -> Image:
    """Resize the image on the given size

    Parameters
    ----------
    img: The image to resize
    size: The size to resize the image

    Returns
    -------

    """
    img = img.resize(size)
    return img


def to_grayscale(img: Image) -> Image:
    """Converts the given image to greyscale

    Parameters
    ----------
    img: The image to convert to grayscale

    Returns
    -------

    A grey-scaled image
    """
    # makes it greyscale
    return ImageOps.grayscale(img)


def to_rgb(image: Image) -> Image:
    """Convert the PIL.Image to RGB. This function
    can be used to convert a PNG image to JPG/JPEG
    formats. Note that this function simply returns the
    converted image. It does not save the newly formatted image

    Parameters
    ----------
    image: The Image to convert

    Returns
    -------

    An Instance of PIL.Image
    """

    # don't convert anything if the
    # image is in the right mode
    if image.mode == 'RGB':
        return image

    return image.convert("RGB")


def chuckify_image_from_path(img: Path, chunk_size: tuple,
                             image_type: ImageLoadersEnumType,
                             output_dir: Path = None,
                             img_format=".jpg") -> List[ImageType]:
    """Create chunks for the image in the given path. Each image will have
    size described in the chunk_size parameter however slightly different chunks may also
    occur. If output_dir is not None, the images will be stored in the specified
    directory as output_dir / img_counter.img_format
    Parameters
    ----------
    img: Path to the image to chunkify
    chunk_size: The chunk size
    image_type: The image type
    output_dir: Where the chunks should be saved
    img_format: The image format for the chunks

    Returns
    -------

    """

    image = load_img(path=img, loader=image_type)

    chunks = chunkify_image(image=image,image_type=image_type, chunk_size=chunk_size)

    if output_dir is not None:
        img_counter = 0
        for chunk in chunks:
            outfile = output_dir / f"img_{img_counter}{img_format}"
            ImageWriters.save_image(image=chunk, image_type=image_type, outpath=outfile)
            img_counter += 1

    return chunks


def chunkify_image(image: ImageType, chunk_size: tuple, image_type: ImageLoadersEnumType) -> List[ImageType]:
    """Create chunks of the given image. Each chunk will be of chunk_size if possible

    Parameters
    ----------
    image: The image to create the chunks for
    chunk_size: The size of the image
    image_type: The image type

    Returns
    -------

    A list of ImageType
    """

    if image_type.value == ImageLoadersEnumType.CV2.value:
        if not isinstance(image, numpy.ndarray):
            raise ValueError(f"image_type is numpy.ndarray but image is {type(image)}")

        img_height, img_width, channels = image.shape
        chunck_width = chunk_size[0]
        chunck_height = chunk_size[1]

        chuncks = []
        for i in range(0, img_height, chunck_height):
            for j in range(0, img_width, chunck_width):
                chunck_data = image[i:i + chunck_height, j:j + chunck_width]
                chuncks.append(chunck_data)

        return chuncks

    raise ValueError(f"Image type {image_type.name} has not been implemented for chunkify_image.")
