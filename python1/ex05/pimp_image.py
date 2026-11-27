from typing import Any
import sys
import numpy as np


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
        and value.ndim == 3
        and value.shape[2] == 3
    ), "The input is not a valid 3D array"


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.

    Args:
        array (np.ndarray): A 3D numpy array representing an image.

    Returns:
        np.ndarray: A new 3D numpy array with inverted colors.

    Raises:
        AssertionError: If the input is not a valid 3D numpy array.
    """
    assert_is_an_image_array(array)
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Extracts the red channel from the image.

    Args:
        array (np.ndarray): A 3D numpy array representing an image.

    Returns:
        np.ndarray: A new 3D numpy array with only the red channel.

    Raises:
        AssertionError: If the input is not a valid 3D numpy array.
    """
    assert_is_an_image_array(array)
    return array * np.array([1, 0, 0], dtype=array.dtype)


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Extracts the green channel from the image.

    Args:
        array (np.ndarray): A 3D numpy array representing an image.

    Returns:
        np.ndarray: A new 3D numpy array with only the green channel.

    Raises:
        AssertionError: If the input is not a valid 3D numpy array.
    """
    assert_is_an_image_array(array)
    result = array.copy()
    result[:, :, 0] = array[:, :, 0] - array[:, :, 0]
    result[:, :, 2] = array[:, :, 2] - array[:, :, 2]
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Extracts the blue channel from the image.

    Args:
        array (np.ndarray): A 3D numpy array representing an image.

    Returns:
        np.ndarray: A new 3D numpy array with only the blue channel.

    Raises:
        AssertionError: If the input is not a valid 3D numpy array.
    """
    assert_is_an_image_array(array)
    result = array.copy()
    result[:, :, :2] = 0
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to greyscale.

    Args:
        array (np.ndarray): A 3D numpy array representing an image.

    Returns:
        np.ndarray: A new 2D numpy array with greyscale values.

    Raises:
        AssertionError: If the input is not a valid 3D numpy array.
    """
    assert_is_an_image_array(array)
    result = np.sum(array, axis=2) / 3
    return result.astype(array.dtype)


# You have some restriction operators for each function:
# (you can only use those given,
# you don’t have to use them all)
# •invert: =, +, -, *
# •red: =, *
# •green: =, -
# •blue: =
# •grey: =, /
