import numpy as np
import torch
from torchvision import transforms
from PIL import Image
from pathlib import Path
from typing import Callable, List, Any, TypeVar, Tuple, Union
from io import BytesIO
import cv2
import os

from mlutils.utils.imgutils.image_enums import ImageFileEnumType, ImageLoadersEnumType, IMAGE_LOADERS_TYPES_STR, IMAGE_STR_TYPES


ImageType = TypeVar("ImageType")


def list_image_files(base_path: Path,
                     valid_exts: Union[List, tuple] = IMAGE_STR_TYPES,
                     contains: str = None) -> Path:
    """Generator that returns all the images in the given
    base_path

    Parameters
    ----------
    base_path: Base path to look for image files
    valid_exts: Extensions to use
    contains: String that the filename should contain

    Returns
    -------

    """

    if isinstance(valid_exts, tuple):
        valid_exts = list(valid_exts)

    for i, item in enumerate(valid_exts):
        if isinstance(item, ImageFileEnumType):
            valid_exts[i] = f'.{item.name.lower()}'

    if not isinstance(valid_exts, tuple):
        valid_exts = tuple(valid_exts)

    # loop over the directory structure
    for (rootDir, dirNames, filenames) in os.walk(base_path):
        # loop over the filenames in the current directory
        for filename in filenames:
            # if the contains string is not none and the filename does not contain
            # the supplied string, then ignore the file
            if contains is not None and filename.find(contains) == -1:
                continue

            # determine the file extension of the current file
            ext = filename[filename.rfind("."):].lower()

            # check to see if the file is an image and should be processed
            if valid_exts is None or ext.endswith(valid_exts):
                # construct the path to the image and yield it
                image_path = os.path.join(rootDir, filename)
                yield Path(image_path)


def get_img_files(base_path: Path,
                  img_formats: Union[List, tuple] = IMAGE_STR_TYPES) -> List[Path]:
    """Get the image files in the given image directory that have
    the specified image format.

    Parameters
    ----------
    base_path: The image directory
    img_formats: The image formats

    Returns
    -------
    An instance of List[Path]
    """

    return list(list_image_files(base_path=base_path, valid_exts=img_formats))


def load_img(path: Path, transformer: Callable = None,
             loader: ImageLoadersEnumType = ImageLoadersEnumType.PIL) -> Any:
    """Load the image from the given path

    Parameters
    ----------
    path: The path to the image
    transformer: Callable object that applies transformations on the image
    loader: How to read the image currently only CV2 or PIL

    Returns
    -------

    If not transform is used it returns an PIL.Image object.
    Otherwise, it returns the datasets type supported by the
    transform
    """

    if loader.name.upper() not in IMAGE_LOADERS_TYPES_STR:
        raise ValueError(f"Invalid image loader={loader.name.upper()} not in {IMAGE_LOADERS_TYPES_STR}")

    if loader.value == ImageLoadersEnumType.PIL.value:
        return load_image_as_pillow(path=path, transformer=transformer)

    if loader.value == ImageLoadersEnumType.PIL_NUMPY.value:
        return load_image_as_numpy(path=path, transformer=transformer)

    if loader.value == ImageLoadersEnumType.CV2.value:
        return load_image_cv2(path=path, transformer=transformer)

    if loader.value == ImageLoadersEnumType.PYTORCH_TENSOR.value:
        return load_image_pytorch_tensor(path=path, transformer=transformer)

    if loader.value == ImageLoadersEnumType.FILEPATH.value:
        return path

    return None


def load_pil_image_from_byte_string(image_byte_string: bytes,
                                    open_if_verify_success: bool = True) -> Image:
    """Loads a PIL.Image from the given byte string

    Parameters
    ----------
    image_byte_string: The byte string representing the image
    open_if_verify_success: Whether to reopen the Image after image.verify()
    is called

    Returns
    -------

    An instance of PIL.Image
    """
    try:
        image = Image.open(BytesIO(image_byte_string))
        image.verify()

        # we need to reopen after verify
        # see this:
        # https://stackoverflow.com/questions/3385561/python-pil-load-throwing-attributeerror-nonetype-object-has-no-attribute-rea
        if open_if_verify_success:
            image = Image.open(BytesIO(image_byte_string))

        return image
    except (IOError, SyntaxError) as e:
        print("ERROR: the image_byte_string is corrupted")
        print(f"Exception message {str(e)}")
        return None


def load_images(path: Path, transformer: Callable = None,
                loader: ImageLoadersEnumType = ImageLoadersEnumType.PIL,
                img_formats: tuple = IMAGE_STR_TYPES) -> List[Any]:
    """Loads all the images in the specified path

    Parameters
    ----------
    path: The path to load the images from
    transformer: how to transform the images
    loader: The type of the laoder either PIL or CV2
    img_formats: The image format

    Returns
    -------
    A list of images. The actual type depends on the type of the
    """

    # get all the image files
    img_files = get_img_files(base_path=path, img_formats=img_formats)

    if len(img_files) == 0:
        raise ValueError(f"{path} does  not have images with formats {img_formats}")

    images = []
    # load every image in the Path
    for img in img_files:
        images.append(load_img(path=img,
                               transformer=transformer,
                               loader=loader))

    return images


def load_images_from_paths(imgs: List[Path], transformer: Callable,
                           loader: ImageLoadersEnumType = ImageLoadersEnumType.PIL) -> List[Any]:
    if len(imgs) == 0:
        raise ValueError("Empty images paths")

    if loader not in IMAGE_LOADERS_TYPES_STR:
        raise ValueError(f"Invalid loader. Loader={loader} not in {IMAGE_LOADERS_TYPES_STR}")

    imgs_data = [load_img(path=img, transformer=transformer, loader=loader) for img in imgs]
    return imgs_data  


def load_image_as_pillow(path: Path, transformer: Callable = None) -> Image:
    """Load the image in the specified path as Pillow.Image object

    Parameters
    ----------
    path
    transformer

    Returns
    -------

    """
    x = Image.open(path)

    if transformer is not None:
        x = transformer(x)
    return x


def load_image_as_numpy(path: Path, transformer: Callable = None) -> np.array:
    x = Image.open(path)
    if transformer is not None:
        x = transformer(x)
    return np.array(x)


def load_image_cv2(path: Path, transformer: Callable = None,
                   with_color=cv2.COLOR_BGR2RGB):
    """Load an image as OpenCV matrix. If WITH_CV2 is False
    throws InvalidConfiguration

    Parameters
    ----------
    path: Path to the image
    transformer: Transformer to apply on loading

    Returns
    -------
    OpenCV image matrix
    """

    image = cv2.imread(str(path))

    if with_color:
        image = cv2.cvtColor(image, code=with_color)

    if transformer is not None:
        image = transformer(image)

    return image


def load_image_pytorch_tensor(path: Path, transformer: Callable = None) -> torch.Tensor:
    """Load the image from the specified path.  If WITH_TORCH is False
    throws InvalidConfiguration

    Parameters
    ----------
    path
    transformer

    Returns
    -------


    """

    with Image.open(path) as image:

        if transformer is None:
            transform_to_torch = transforms.Compose([transforms.ToTensor()])
            return transform_to_torch(image)

        x = image
        x = transformer(x)

        if isinstance(x, torch.Tensor):
            return x

        transform_to_torch = transforms.Compose([transforms.ToTensor()])
        return transform_to_torch(x)
   

def load_images_as_torch(x: List[Path], y_train: List[int],
                         transformer: Callable) -> tuple:
    """Load the images in the path as torch tensors

    Parameters
    ----------
    x: A list of image files
    y_train: The labels associated with evey image
    transformer: Transform to apply when loading the images.
    Usually this will be transforms.Compose

    Returns
    -------
    A tuple of torch.Tensors
    """

    data = [load_img(img_path, transformer) for img_path in x]
    return torch.stack(data), torch.tensor(y_train, dtype=torch.uint8)


class ImageWriters:

    @staticmethod
    def save_image(image: ImageType, image_type: ImageLoadersEnumType, outpath: Path) -> None:

        if image_type == ImageLoadersEnumType.CV2:
            cv2.imwrite(str(outpath), image)

        else:
            raise ValueError("Not implemented yet")

    @staticmethod
    def save_images(images: List[Tuple[ImageType, Path]]):
        for img in images:
            ImageWriters.save_image(image=img[0], outpath=img[1])
