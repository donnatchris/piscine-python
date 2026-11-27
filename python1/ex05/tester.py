import numpy as np
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from matplotlib import pyplot as plt


def print_image(img_array: np.ndarray, title: str = "") -> None:
    """
    Display the image using matplotlib.

    Args:
        img_array (np.ndarray): The input image array.

    Raises:
        AssertionError: If the input value is not a valid 3D numpy array.
    """
    plt.imshow(img_array, cmap="grey", vmin=0, vmax=255)
    plt.title(title)
    plt.show()


array = ft_load("landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)


print_image(array, "Original")
print_image(ft_invert(array), "Invert")
print_image(ft_red(array), "Red")
print_image(ft_green(array), "Green")
print_image(ft_blue(array), "Blue")
print_image(ft_grey(array), "Grey")


# Expected output: (docstrings can be different)
# $> python tester.py
# The shape of image is: (257, 450, 3)
# [[[19 42 83]
# [23 42 84]
# [28 43 84]
# ...
# [ 0 0 0]
# [ 1 1 1]
# [ 1 1 1]]]
# ...
# Inverts the color of the image received.
# $>
