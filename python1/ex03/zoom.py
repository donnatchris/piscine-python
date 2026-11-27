from typing import Any
import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def assert_is_an_image_array(value: Any) -> None:
    """
    Validate a non-empty 3D image array with one or three channels.

    Args:
        value (Any): The input value to check.

    Raises:
        AssertionError: If the input is not a non-empty 3D NumPy array
            with one or three channels.
    """
    assert (
        isinstance(value, np.ndarray)
        and value.ndim == 3
        and value.size > 0
        and value.shape[2] in (1, 3)
    ), "The image must be a non-empty 3D array with one or three channels."


def zoom(img_array: np.ndarray) -> np.ndarray:
    """
    Crop the top-left corner to at most 400x400 pixels and keep one channel.

    Print the cropped shape, or an error message if validation fails.

    Args:
        img_array (np.ndarray): A non-empty 3D array with one or three
            channels.

    Returns:
        np.ndarray: The cropped array with one channel,
            or an empty array if input validation fails.
    """
    try:
        assert_is_an_image_array(img_array)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return np.array([])

    zoomed = img_array[:400, :400, :1]
    print(
        f"New shape after slicing: {zoomed.shape} "
        f"or {zoomed.squeeze(axis=2).shape}"
    )
    return zoomed


def print_image(img_array: np.ndarray) -> None:
    """
    Display the image using matplotlib.

    Print an error message and return without displaying the image if
    validation fails. Matplotlib errors propagate to the caller.

    Args:
        img_array (np.ndarray): A non-empty 3D array with one or three
            channels.
    """
    try:
        assert_is_an_image_array(img_array)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    plt.imshow(img_array, cmap="grey", vmin=0, vmax=255)
    plt.show()


def main() -> None:
    """Load, crop and display animal.jpeg, reporting processing errors."""
    try:
        path = "animal.jpeg"
        img_array = ft_load(path)
        if img_array.size == 0:
            return
        print(img_array)
        zoomed = zoom(img_array)
        if zoomed.size == 0:
            return
        print(zoomed)
        print_image(zoomed)
    except Exception as e:
        print(f"Error processing image: {e}")


if __name__ == "__main__":
    main()
