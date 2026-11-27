import numpy as np
from PIL import Image


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

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return np.array([])

    try:
        with Image.open(path) as img:
            img_rgb = img.convert("RGB")
            img_array = np.array(img_rgb)
            print(f"The shape of image is: {img_array.shape}")
            return img_array

    except Exception as e:
        print(f"Error loading image: {e}")
        return np.array([])


def main() -> None:
    """
    Main function to test the ft_load function.
    It loads an image and prints its shape and pixel values.
    """
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()


# Expected output:
# $> python tester.py
# The shape of image is: (257, 450, 3)
# [[[19 42 83]
# [23 42 84]
# [28 43 84]
# ...
# [ 0 0 0]
# [ 1 1 1]
# [ 1 1 1]]]
# $>
