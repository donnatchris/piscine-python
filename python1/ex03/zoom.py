from typing import Any
import numpy as np
import sys
from matplotlib import pyplot as plt
from load_image import ft_load


def print_error(error: Exception) -> None:
    """
    Print an error message to stderr.
    """
    print(f"Error: {error}", file=sys.stderr)


def assert_is_an_image_array(value: Any) -> None:
    """
    Assert that the input value is
    a valid 3D numpy array representing an image.

    Args:
        value (Any): The input value to check.

    Raises:
        AssertionError: If the input value is not a valid 3D numpy array.
    """
    assert (
        isinstance(value, np.ndarray)
        and value.ndim > 1
        and value.ndim < 4
    ), "The input is not a valid 3D array"


def zoom(img_array: np.ndarray) -> np.ndarray:
    """
    Zoom into the top-left corner of the image
    by cropping it to 400x400 pixels.

    Args:
        img_array (np.ndarray): The input image array.

    Returns:
        np.ndarray: The cropped image array.
    """
    assert_is_an_image_array(img_array)
    zoomed = img_array[:400, :400, :1]
    print(f"New shape after slicing:\
          {zoomed.shape} or {zoomed.squeeze(axis=2).shape}")
    return zoomed


def print_image(img_array: np.ndarray) -> None:
    """
    Display the image using matplotlib.

    Args:
        img_array (np.ndarray): The input image array.

    Raises:
        AssertionError: If the input value is not a valid 3D numpy array.
    """
    assert_is_an_image_array(img_array)
    plt.imshow(img_array, cmap="grey", vmin=0, vmax=255)
    plt.show()


def main() -> None:
    """
Main function to load an image, zoom into it, and display the result.
    """
    try:
        path = "animal.jpeg"
        img_array = ft_load(path)
        print(img_array)
        zoomed = zoom(img_array)
        print(zoomed)
        print_image(zoomed)

    except Exception as e:
        print_error(e)


if __name__ == "__main__":
    main()
