from typing import Union
from PIL.Image import Image as PILImage
from PIL import ImageFilter
import numpy as np

from mlutils.utils.imgutils.image_transformers import pil_image_from_array


def edge_detector(image: Union[PILImage, np.ndarray]) -> PILImage:

    if isinstance(image, PILImage):
        edges = image.filter(ImageFilter.FIND_EDGES)
        return edges

    if isinstance(image, np.ndarray):
        new_image = pil_image_from_array(image)
        edges = new_image.filter(ImageFilter.FIND_EDGES)
        return edges

    raise ValueError("The provided image should either be a Pillow Image or a numpy array")