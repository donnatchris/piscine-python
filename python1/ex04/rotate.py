from typing import Any
import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def print_error(error: Exception) -> None:
    """Print a clear error message."""
    print(f"Error: {error}")


def assert_is_an_image_array(value: Any) -> None:
    """
    Validate a non-empty 2D or 3D image array.

    Args:
        value (Any): The input value to check.

    Raises:
        AssertionError: If the input is not a non-empty 2D NumPy array
            or a non-empty 3D NumPy array with one or three channels.
    """
    assert (
        isinstance(value, np.ndarray)
        and value.ndim in (2, 3)
        and value.size > 0
        and (value.ndim == 2 or value.shape[2] in (1, 3))
    ), "The image must be non-empty, 2D or 3D with one or three channels."


def transpose(img_array: np.ndarray) -> np.ndarray:
    """
    Crop a square from the top-left corner and transpose it manually.

    Use at most 400 pixels per side and retain the first channel of a 3D
    image. Print the cropped shape and pixels, then the transposed shape.
    Print an error message and return an empty array if validation fails.

    Args:
        img_array (np.ndarray): A non-empty 2D image or a 3D image with
            one or three channels.

    Returns:
        np.ndarray: The transposed 2D square, or an empty array if input
            validation fails.
    """
    try:
        assert_is_an_image_array(img_array)
    except AssertionError as e:
        print_error(e)
        return np.array([])

    size = min(400, img_array.shape[0], img_array.shape[1])
    if img_array.ndim == 3:
        square = img_array[:size, :size, :1]
        pixels = square[:, :, 0]
        print(f"The shape of image is: {square.shape} or {pixels.shape}")
    else:
        square = img_array[:size, :size]
        pixels = square
        print(f"The shape of image is: {square.shape}")
    print(square)

    rotated = np.empty((size, size), dtype=pixels.dtype)
    for y in range(size):
        for x in range(size):
            rotated[x, y] = pixels[y, x]
    print(f"New shape after Transpose: {rotated.shape}")
    return rotated


def print_image(img_array: np.ndarray) -> None:
    """
    Display a validated image using Matplotlib.

    Print an error message and return without displaying the image if
    validation fails. Matplotlib errors propagate to the caller.

    Args:
        img_array (np.ndarray): A non-empty 2D image or a 3D image with
            one or three channels.
    """
    try:
        assert_is_an_image_array(img_array)
    except AssertionError as e:
        print_error(e)
        return
    plt.imshow(img_array, cmap="grey", vmin=0, vmax=255)
    plt.show()


def main() -> None:
    """Load animal.jpeg and print and display its transposed square crop.

    Report processing and display errors without terminating abruptly.
    """
    path = "animal.jpeg"
    img_array = ft_load(path)
    if img_array.size == 0:
        return
    transposed = transpose(img_array)
    if transposed.size == 0:
        return
    print(transposed)
    print_image(transposed)


if __name__ == "__main__":
    main()
