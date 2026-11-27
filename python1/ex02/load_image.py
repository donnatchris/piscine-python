import numpy as np
from PIL import Image
import sys


def print_error(error: Exception) -> None:
    """
    Print an error message to stderr.
    """
    print(f"Error: {error}", file=sys.stderr)


def ft_load(path: str) -> np.ndarray:
    """
    Load an image, prints its shape and return its RGB pixels.

    Args:
        path (str): The path to the image.

    Returns:
        np.ndarray: The RGB pixel values of the image,
        or an empty array if an error occurs.
    """
    try:
        assert isinstance(path, str), "Path must be a string"
        with Image.open(path) as img:
            img_rgb = img.convert("RGB")
            img_array = np.array(img_rgb)
            print(f"The shape of image is: {img_array.shape}")
            return img_array

    except Exception as e:
        print_error(e)
        return np.array([])
