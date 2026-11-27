from typing import Any
import numpy as np


def get_arg_error() -> str:
    """
    Returns an error string.

    Returns:
        str: The error string.
    """
    return "the arguments are bad"


def assert_is_int(value: Any) -> None:
    """
    Validates that the argument is an integer.

    Args:
        value (Any): the value to check.

    Raises:
        AssertionError: if the argument is not an int.
    """
    assert type(value) is int, get_arg_error()


def assert_is_number(value: Any) -> None:
    """
    Validates that the argument is a number.

    Args:
        value (Any): the value to check.

    Raises:
        AssertionError: if the argument is not an int or a float.
    """
    assert type(value) in (int, float), get_arg_error()


def assert_is_positive_number(value: Any) -> None:
    """
    Validates that the argument is a positive number.

    Args:
        value (Any): the value to check.

    Raises:
        AssertionError: if the argument is not a positive number.
    """
    assert_is_number(value)
    assert value > 0, get_arg_error()


def assert_is_list(value: Any) -> None:
    """
    Validates that the argument is a list.

    Args:
        value (Any): the value to check.

    Raises:
        AssertionError: if the argument is not a list.
    """
    assert isinstance(value, list), get_arg_error()


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
    assert len(value_1) == len(value_2), get_arg_error()


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """
    Take a list of heights and a list of weights and return BMI values.

    Args:
        height (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kg.

    Returns:
        list[int | float]: A list of BMI values.

    Raises:
        AssertionError: If the arguments are not lists, have different
            lengths, contain non-numeric elements, or contain negative
            or zero values.
    """

    assert_are_lists_of_same_len(height, weight)
    assert_is_positive_number_list(height)
    assert_is_positive_number_list(weight)

    h_array = np.array(height, dtype=float)
    w_array = np.array(weight, dtype=float)

    return (w_array / h_array ** 2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Take a list of numeric values and a single number as limit
    and returns a list of booleans:
    True if the value is above the limit, False if not.

    Args:
        bmi (list[int | float]): A list of bmi.
        limit (int): A numeric threshold.

    Returns:
        list[bool]: A list of booleans.

    Raises:
        AssertionError: If the arguments are not a list of numeric values
        and a numeric value.
    """

    assert_is_list(bmi)
    assert_is_int(limit)

    bmi_array = np.array(bmi)
    return (bmi_array > limit).tolist()
