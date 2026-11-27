import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image, print its shape and pixels, and return its RGB array.

    Print an error message and return an empty array if loading fails.

    Args:
        path (str): The path to the image.

    Returns:
        np.ndarray: The RGB pixel values of the image,
        or an empty array if an error occurs.
    """
    try:
        assert isinstance(path, str), "Path must be a string"

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return np.array([])

    try:
        with Image.open(path) as img:
            img_rgb = img.convert("RGB")
            img_array = np.array(img_rgb)
            print(f"The shape of image is: {img_array.shape}")
            print(img_array)
            return img_array

    except Exception as e:
        print(f"Error loading image: {e}")
        return np.array([])
