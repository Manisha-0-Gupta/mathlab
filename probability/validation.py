"""
Shared input checks for the whole probability package

"""

import math


def check_real_number(value, name):
    """Real, finite number, bool is not allowed (True would act like 1)"""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number,got {type(value).__name__}")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite, got {value}")


def check_integer(value, name):
    """Whole number, bool is not allowed."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} msut be an integer, got {type(value).__name__}")


def check_positive_integer(value, name):
    """Whole number greater than 0. Use for trials,n, number of samples"""
    check_integer(value, name)
    if value <= 0:
        raise ValueError(f"{name} must be nonzero positive integer,got {value}")


def check_non_negative_integer(value, name):
    """Whole number 0 or more. Use for k in pmf or cdf"""
    check_integer(value, name)
    if value < 0:
        raise ValueError(f"{name} must be 0 or more, got {value}")


def check_positive_real_number(value, name):
    """Number greater than 0. Use for rate,lambda,sigma,shape"""
    check_real_number(value, name)
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0, got {value}")


def check_probability_value(value, name):
    """Number between 0 and 1 , including both ends"""
    check_real_number(value, name)
    if not 0 <= value <= 1:
        raise ValueError(f"{name} must be between 0 and 1,got {value}")


def check_empty_data(data, name="data"):
    """List or other sequence with at least one item"""
    if len(data) == 0:
        raise ValueError(f"{name} must not be empty")
