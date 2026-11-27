import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Print the original and sliced shapes and return the sliced rows.

    Convert the input to a NumPy array before slicing. This conversion
    may coerce the types and values of the input elements.
    Print an error message and return an empty list if input validation
    or NumPy array conversion fails.

    Args:
        family (list): A 2D list whose rows have equal lengths.
        start (int): Inclusive starting row index. May be negative.
        end (int): Exclusive ending row index. May be negative.

    Returns:
        list: The sliced NumPy array converted back to a list.
            An empty list if the slice is empty, validation fails,
            or array conversion fails.
    """
    try:
        assert (
            isinstance(family, list)
            and type(start) is int
            and type(end) is int
        ), "First argument must be a list, \
            second and third arguments must be integers."

        assert all(
            isinstance(row, list) for row in family
        ), "All elements of the first argument must be lists."

        assert all(
            len(row) == len(family[0]) for row in family
        ), "All rows in the first argument must have the same length."

    except Exception as e:
        print(f"AssertionError: {e}")
        return []

    try:
        family_array = np.array(family)

    except Exception as e:
        print(f"Error converting to numpy array: {e}")
        return []

    try:
        assert family_array.ndim == 2, "The first argument must be a 2D list."

    except Exception as e:
        print(f"AssertionError: {e}")
        return []

    sliced_array = family_array[start:end]

    print(f"My shape is : {family_array.shape}")
    print(f"My new shape is : {sliced_array.shape}")

    return family[start:end]


def main() -> None:
    """Run and print two slicing examples, including a negative end index."""
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()


# Expected output:
# $> python test_array2D.py
# My shape is : (4, 2)
# My new shape is : (2, 2)
# [[1.8, 78.4], [2.15, 102.7]]
# My shape is : (4, 2)
# My new shape is : (1, 2)
# [[2.15, 102.7]]
# $
