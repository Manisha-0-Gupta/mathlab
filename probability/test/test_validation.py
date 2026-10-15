import math

import pytest

from probability.validation import (
    check_empty_data,
    check_integer,
    check_non_negative_integer,
    check_positive_integer,
    check_positive_real_number,
    check_probability_value,
    check_real_number,
)

# check_real_number


@pytest.mark.parametrize("value", [0, 1, -5, 2.5, -3.7])
def test_check_real_number_valid(value):
    check_real_number(value, "value")


@pytest.mark.parametrize("value", [True, False, "5", None, [1, 2]])
def test_check_real_number_invalid_type(value):
    with pytest.raises(TypeError):
        check_real_number(value, "value")


@pytest.mark.parametrize("value", [math.inf, -math.inf, math.nan])
def test_check_real_number_non_finite(value):
    with pytest.raises(ValueError):
        check_real_number(value, "value")


# check_integer


@pytest.mark.parametrize("value", [0, 1, -5, 100])
def test_check_integer_valid(value):
    check_integer(value, "value")


@pytest.mark.parametrize("value", [True, False, 2.5, "5", None])
def test_check_integer_invalid(value):
    with pytest.raises(TypeError):
        check_integer(value, "value")


# check_positive_integer


@pytest.mark.parametrize("value", [1, 2, 100])
def test_check_positive_integer_valid(value):
    check_positive_integer(value, "value")


@pytest.mark.parametrize("value", [0, -1, -100])
def test_check_positive_integer_non_positive(value):
    with pytest.raises(ValueError):
        check_positive_integer(value, "value")


def test_check_positive_integer_invalid_type():
    with pytest.raises(TypeError):
        check_positive_integer(2.5, "value")


# check_non_negative_integer


@pytest.mark.parametrize("value", [0, 1, 100])
def test_check_non_negative_integer_valid(value):
    check_non_negative_integer(value, "value")


@pytest.mark.parametrize("value", [-1, -10])
def test_check_non_negative_integer_negative(value):
    with pytest.raises(ValueError):
        check_non_negative_integer(value, "value")


def test_check_non_negative_integer_invalid_type():
    with pytest.raises(TypeError):
        check_non_negative_integer(True, "value")


# check_positive_real_number


@pytest.mark.parametrize("value", [0.1, 1, 2.5, 100])
def test_check_positive_real_number_valid(value):
    check_positive_real_number(value, "value")


@pytest.mark.parametrize("value", [0, -1, -2.5])
def test_check_positive_real_number_non_positive(value):
    with pytest.raises(ValueError):
        check_positive_real_number(value, "value")


def test_check_positive_real_number_invalid_type():
    with pytest.raises(TypeError):
        check_positive_real_number("2.5", "value")


def test_check_positive_real_number_non_finite():
    with pytest.raises(ValueError):
        check_positive_real_number(math.inf, "value")


# check_probability_value


@pytest.mark.parametrize("value", [0, 0.25, 0.5, 1])
def test_check_probability_value_valid(value):
    check_probability_value(value, "value")


@pytest.mark.parametrize("value", [-0.1, 1.1, -5, 2])
def test_check_probability_value_out_of_range(value):
    with pytest.raises(ValueError):
        check_probability_value(value, "value")


def test_check_probability_value_invalid_type():
    with pytest.raises(TypeError):
        check_probability_value(True, "value")


# check_empty_data


@pytest.mark.parametrize("data", [[1], [1, 2, 3], (1, 2), "abc"])
def test_check_empty_data_valid(data):
    check_empty_data(data)


@pytest.mark.parametrize("data", [[], (), ""])
def test_check_empty_data_empty(data):
    with pytest.raises(ValueError):
        check_empty_data(data)


def test_check_empty_data_custom_name():
    with pytest.raises(ValueError, match="observations must not be empty"):
        check_empty_data([], "observations")
