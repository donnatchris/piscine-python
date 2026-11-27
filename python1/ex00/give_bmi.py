from typing import Any
import numpy as np


def assert_is_int(value: Any) -> None:
    """
    Validates that the argument is an integer.

    Args:
        value (Any): the value to check.

    Raises:
        AssertionError: if the argument is not an int.
    """
    assert type(value) is int, "The argument must be an integer."


def assert_is_number(value: Any) -> None:
    """
    Validates that the argument is a number.

    Args:
        value (Any): the value to check.

    Raises:
        AssertionError: if the argument is not an int or a float.
    """
    assert (
        type(value) in (int, float)
    ), "The argument must be a number (int or float)."


def assert_is_positive_number(value: Any) -> None:
    """
    Validates that the argument is a positive number.

    Args:
        value (Any): the value to check.

    Raises:
        AssertionError: if the argument is not a positive number.
    """
    assert_is_number(value)
    assert value > 0, "The argument must be a positive number."


def assert_is_list(value: Any) -> None:
    """
    Validates that the argument is a list.

    Args:
        value (Any): the value to check.

    Raises:
        AssertionError: if the argument is not a list.
    """
    assert isinstance(value, list), "The argument must be a list."


def assert_is_number_list(value: Any) -> None:
    """
    Validates that the argument is a list of numbers.

    Args:
        value (Any): the value to check.

    Raises:
        AssertionError: if the argument is not a list of numbers.
    """
    assert_is_list(value)
    for v in value:
        assert_is_number(v)


def assert_is_positive_number_list(value: Any) -> None:
    """
    Validates that the argument is a list of positive numbers.

    Args:
        value (Any): the value to check.

    Raises:
        AssertionError: if the argument is not a list of positive numbers.
    """
    assert_is_list(value)
    for v in value:
        assert_is_positive_number(v)


def assert_are_lists_of_same_len(value_1: Any, value_2: Any) -> None:
    """
    Validates that both arguments are lists of equal length.

    Args:
        value_1 (Any) and value_2 (Any): the 2 arguments to check and compare.

    Raises:
        AssertionError: if the arguments are not lists,
        or if they do not have the same length.
    """
    assert_is_list(value_1)
    assert_is_list(value_2)
    assert len(value_1) == len(value_2), "The lists must have the same length."


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculate BMI values from lists of heights and weights.

    Print an error message and return an empty list if input validation
    or NumPy array conversion fails.

    Args:
        height (list[int | float]): Positive heights in meters.
        weight (list[int | float]): Positive weights in kilograms.
            Must have the same length as height.

    Returns:
        list[int | float]: BMI values, or an empty list if the input lists
            are empty, validation fails, or array conversion fails.
    """

    try:
        assert_are_lists_of_same_len(height, weight)
        assert_is_positive_number_list(height)
        assert_is_positive_number_list(weight)
    except Exception as e:
        print(f"Invalid input: {e}")
        return []

    try:
        h_array = np.array(height, dtype=float)
        w_array = np.array(weight, dtype=float)
    except Exception as e:
        print(f"Error converting to numpy arrays: {e}")
        return []

    return (w_array / h_array ** 2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return whether each BMI value is strictly greater than an integer limit.

    Print an error message and return an empty list if input validation
    or NumPy array conversion fails.

    Args:
        bmi (list[int | float]): BMI values to compare.
        limit (int): An integer threshold.

    Returns:
        list[bool]: True for values above the limit, False otherwise.
            An empty list if bmi is empty, validation fails,
            or array conversion fails.
    """

    try:
        assert_is_number_list(bmi)
        assert_is_int(limit)
    except Exception as e:
        print(f"Invalid input: {e}")
        return []

    try:
        bmi_array = np.array(bmi)
    except Exception as e:
        print(f"Error converting to numpy array: {e}")
        return []

    return (bmi_array > limit).tolist()


def main() -> None:
    """
    Main function to test the give_bmi and apply_limit functions.
    It creates sample height and weight lists, calculates BMI values,
    and applies a limit to the BMI values, printing the results.
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
