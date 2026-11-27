from typing import Any
import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def print_error(error: Exception) -> None:
    """Print a clear error message."""
    print(f"Error: {error}")


def assert_is_an_image_array(value: Any) -> None:
    """Validate a non-empty RGB NumPy array.

    Args:
        value (Any): The input value to check.

    Raises:
        AssertionError: If the input is not a non-empty 3D NumPy array
            with three channels.
    """
    assert (
        isinstance(value, np.ndarray)
        and value.ndim == 3
        and value.size > 0
        and value.shape[2] == 3
    ), "The image must be a non-empty 3D array with three RGB channels."


def print_image(img_array: np.ndarray, title: str = "") -> bool:
    """Display an RGB image and report validation or display errors.

    Args:
        img_array (np.ndarray): A non-empty RGB image array.
        title (str): The title displayed above the image.

    Returns:
        bool: True if the image was displayed, False if an error occurred.
    """
    figure = None
    try:
        assert_is_an_image_array(img_array)
        figure = plt.figure()
        plt.imshow(img_array)
        plt.title(title)
        plt.show()
        return True
    except Exception as e:
        print_error(e)
        return False
    finally:
        if figure is not None:
            plt.close(figure)


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Invert and display the colors of an RGB image.

    Print an error message if validation, filtering or display fails.

    Args:
        array (np.ndarray): A non-empty RGB image array.

    Returns:
        np.ndarray: A new inverted array with the same shape as the input,
            or an empty array if an error occurs.
    """
    try:
        assert_is_an_image_array(array)
        result = 255 - array
        if not print_image(result, "Invert"):
            return np.array([])
        return result
    except Exception as e:
        print_error(e)
        return np.array([])


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep and display only the red channel of an RGB image.

    Print an error message if validation, filtering or display fails.

    Args:
        array (np.ndarray): A non-empty RGB image array.

    Returns:
        np.ndarray: A new red-only array with the same shape as the input,
            or an empty array if an error occurs.
    """
    try:
        assert_is_an_image_array(array)
        result = array * np.array([1, 0, 0], dtype=array.dtype)
        if not print_image(result, "Red"):
            return np.array([])
        return result
    except Exception as e:
        print_error(e)
        return np.array([])


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep and display only the green channel of an RGB image.

    Print an error message if validation, filtering or display fails.

    Args:
        array (np.ndarray): A non-empty RGB image array.

    Returns:
        np.ndarray: A new green-only array with the same shape as the input,
            or an empty array if an error occurs.
    """
    try:
        assert_is_an_image_array(array)
        result = array.copy()
        result[:, :, 0] = array[:, :, 0] - array[:, :, 0]
        result[:, :, 2] = array[:, :, 2] - array[:, :, 2]
        if not print_image(result, "Green"):
            return np.array([])
        return result
    except Exception as e:
        print_error(e)
        return np.array([])


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep and display only the blue channel of an RGB image.

    Print an error message if validation, filtering or display fails.

    Args:
        array (np.ndarray): A non-empty RGB image array.

    Returns:
        np.ndarray: A new blue-only array with the same shape as the input,
            or an empty array if an error occurs.
    """
    try:
        assert_is_an_image_array(array)
        result = array.copy()
        result[:, :, :2] = 0
        if not print_image(result, "Blue"):
            return np.array([])
        return result
    except Exception as e:
        print_error(e)
        return np.array([])


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert and display an RGB image in greyscale with three channels.

    Print an error message if validation, filtering or display fails.

    Args:
        array (np.ndarray): A non-empty RGB image array.

    Returns:
        np.ndarray: A new grey array with the same shape as the input,
            or an empty array if an error occurs.
    """
    try:
        assert_is_an_image_array(array)
        grey = np.sum(array, axis=2, keepdims=True) / 3
        result = np.repeat(grey, 3, axis=2).astype(array.dtype)
        if not print_image(result, "Grey"):
            return np.array([])
        return result
    except Exception as e:
        print_error(e)
        return np.array([])


def main() -> None:
    """Load landscape.jpg and display the original and all five filters.

    Print the inversion function's documentation after displaying the images.
    Stop with a clear message if loading, filtering or display fails.
    """
    try:
        array = ft_load("landscape.jpg")
        if array.size == 0:
            return
        if not print_image(array, "Original"):
            return
        for image_filter in (ft_invert, ft_red, ft_green, ft_blue, ft_grey):
            if image_filter(array).size == 0:
                return
        print(ft_invert.__doc__)
    except Exception as e:
        print_error(e)


if __name__ == "__main__":
    main()
