import numpy as np


def get_arg_error() -> str:
    """
    Returns an error string.

    Returns:
        str: The error string.
    """
    return "the arguments are bad"


def slice_me(family: list, start: int, end: int) -> list:
    """
    Print the shape of the list passed as first argument,
    slice the list from the start argument to the end argument,
    print the shape of the sliced list
    and returns that sliced list.

    Args:
        family (list): a 2D list.
        start (int): the integer used to slice the list.
        end (int): the integer used to slice the list.

    Raises:
        AssertionError: if the first argument is not a 2D list,
        or if the others arguments are not integers.
    """
    assert (
        isinstance(family, list)
        and type(start) is int
        and type(end) is int
    ), get_arg_error()

    assert all(
        isinstance(row, list) for row in family
    ), get_arg_error()

    assert all(
        len(row) == len(family[0]) for row in family
    ), get_arg_error()

    family_array = np.array(family)

    assert family_array.ndim == 2, get_arg_error()

    sliced_array = family_array[start:end]

    print(f"My shape is : {family_array.shape}")
    print(f"My new shape is : {sliced_array.shape}")

    return sliced_array.tolist()
