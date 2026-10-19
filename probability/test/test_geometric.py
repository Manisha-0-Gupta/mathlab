import math
import random

import pytest

from probability.geometric import GeometricDistribution
from probability.simulations.geometric_simulation import (
    geometric_sampler,
    geometric_simulation,
    probability_of_success_at_first_or_third_try,
)
from probability.simulations.simulation import (
    empirical_cdf,
    empirical_mean,
    empirical_pmf,
    empirical_variance,
)


def test_valid_probability():

    GeometricDistribution(0.5)
    GeometricDistribution(1)


def test_invalid_probability():

    try:
        GeometricDistribution(0)
        assert False
    except ValueError:
        assert True

    try:
        GeometricDistribution(1.5)
        assert False
    except ValueError:
        assert True


distribution = GeometricDistribution(0.7)


def test_pmf():

    assert math.isclose(distribution.pmf(1), 0.7)
    assert math.isclose(distribution.pmf(2), 0.21)
    assert math.isclose(distribution.pmf(3), 0.063)
    assert math.isclose(distribution.pmf(5), 0.00567)


def test_invalid_k():

    try:
        distribution.pmf(0)
        assert False
    except ValueError:
        assert True

    try:
        distribution.pmf(2.5)
        assert False
    except ValueError:
        assert True


def test_expected_value():
    assert math.isclose(distribution.expected_value(), 1 / 0.7)


def test_variance():
    assert math.isclose(distribution.variance(), 0.3 / (0.7**2))


def test_standard_deviation():
    expected = (0.3 / (0.7**2)) ** 0.5
    assert math.isclose(distribution.standard_deviation(), expected)


def test_cdf():
    distribution = GeometricDistribution(0.7)

    assert math.isclose(distribution.cdf(1), 0.7)
    assert math.isclose(distribution.cdf(3), 0.973)
    assert math.isclose(distribution.cdf(5), 0.99757)
    assert distribution.cdf(0) == 0


"""----------------------------------------------------------------------------------------------------------------"""
"""TEST-GEOMETRIC-SIMULATION"""
"""----------------------------------------------------------------------------------------------------------------"""


def test_geometric_sampler():
    # success at first try
    result = geometric_sampler(0.7, lambda: 0.5)
    assert result == 1

    # success at x = 4
    values = iter([0.7, 0.6, 0.7, 0.4])
    result = geometric_sampler(0.5, lambda: next(values))
    assert result == 4
    # p = 0
    with pytest.raises(ValueError):
        geometric_sampler(0, lambda: 0.5)

    # invalid_random_value
    with pytest.raises(ValueError):
        geometric_sampler(0.5, lambda: 2)


def test_geometric_simulation():
    # invalid_trials
    with pytest.raises(ValueError):
        geometric_simulation(0, 0.5, lambda: 0.1)

    # deterministic simulation
    values = iter([0.1, 0.6, 0.2, 0.7, 0.8, 0.3])

    data = geometric_simulation(3, 0.5, lambda: next(values))

    assert data == [1, 2, 3]


def test_statistical_calculation():
    rng = random.Random(42)
    g_d = GeometricDistribution(0.7)
    data = geometric_simulation(10_000, 0.7, rng.random)

    # empirical_mean
    assert math.isclose(g_d.expected_value(), empirical_mean(data), abs_tol=0.05)

    # empirical_variation
    assert math.isclose(g_d.variance(), empirical_variance(data), abs_tol=0.05)

    # empirical_pmf
    assert math.isclose(g_d.pmf(3), empirical_pmf(data, 3), abs_tol=0.05)

    # empirical_cdf
    assert math.isclose(g_d.cdf(3), empirical_cdf(data, 3), abs_tol=0.05)


def test_probability_of_success_at_first_or_third_try():
    rng = random.Random(42)
    g_d = GeometricDistribution(0.7)
    _, __, estimated_probability = probability_of_success_at_first_or_third_try(
        10_000, 0.7, rng.random
    )

    assert math.isclose(g_d.pmf(1) + g_d.pmf(3), estimated_probability, abs_tol=0.05)
