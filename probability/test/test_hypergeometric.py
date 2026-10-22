import math
import random

import pytest

from probability.hypergeometric import HyperGeometric
from probability.simulations.hypergeometric_simulation import (
    hypergeometric_sampler,
    hypergeometric_simulation,
)
from probability.simulations.simulation import (
    empirical_cdf,
    empirical_mean,
    empirical_pmf,
    empirical_variance,
)


def test_valid_parameters():
    HyperGeometric(10, 4, 3)
    HyperGeometric(20, 10, 5)
    HyperGeometric(1, 0, 0)
    HyperGeometric(1, 1, 1)


def test_invalid_N():
    try:
        HyperGeometric(0, 0, 0)
        assert False
    except ValueError:
        assert True

    try:
        HyperGeometric(-1, 0, 0)
        assert False
    except ValueError:
        assert True

    try:
        HyperGeometric(10.5, 4, 3)
        assert False
    except ValueError:
        assert True


def test_invalid_K():
    try:
        HyperGeometric(10, -1, 3)
        assert False
    except ValueError:
        assert True

    try:
        HyperGeometric(10, 11, 3)
        assert False
    except ValueError:
        assert True

    try:
        HyperGeometric(10, 4.5, 3)
        assert False
    except ValueError:
        assert True


def test_invalid_n():
    try:
        HyperGeometric(10, 4, -1)
        assert False
    except ValueError:
        assert True

    try:
        HyperGeometric(10, 4, 11)
        assert False
    except ValueError:
        assert True

    try:
        HyperGeometric(10, 4, 3.5)
        assert False
    except ValueError:
        assert True


def test_pmf():
    distribution = HyperGeometric(10, 4, 3)

    # P(X = 0)
    assert math.isclose(distribution.pmf(0), 0.1666666667)

    # P(X = 1)
    assert math.isclose(distribution.pmf(1), 0.5)

    # P(X = 2)
    assert math.isclose(distribution.pmf(2), 0.3)

    # P(X = 3)
    assert math.isclose(distribution.pmf(3), 0.03333333333333333)


def test_invalid_k():
    distribution = HyperGeometric(10, 4, 3)

    try:
        distribution.pmf(-1)
        assert False
    except ValueError:
        assert True

    try:
        distribution.pmf(4)
        assert False
    except ValueError:
        assert True

    try:
        distribution.pmf(1.5)
        assert False
    except TypeError:
        assert True


def test_statistics():
    distribution = HyperGeometric(10, 4, 3)

    assert math.isclose(distribution.expected_value(), 1.2)
    assert math.isclose(distribution.variance(), 0.56)
    assert math.isclose(distribution.standard_deviation(), math.sqrt(0.56))


def test_cdf():
    distribution = HyperGeometric(10, 4, 3)

    assert math.isclose(distribution.cdf(0), 0.1666666667)
    assert math.isclose(distribution.cdf(1), 0.6666666667)
    assert math.isclose(distribution.cdf(2), 0.9666666667)
    assert math.isclose(distribution.cdf(3), 1.0)


def test_cdf_boundaries():
    distribution = HyperGeometric(10, 4, 3)

    assert distribution.cdf(-1) == 0
    assert distribution.cdf(4) == 1

    try:
        distribution.cdf(1.5)
        assert False
    except TypeError:
        assert True


"""---------------------------------------------------------------------------------------------------------"""
"""TEST-HYPERGEOMETRIC-SIMULATION"""
"""---------------------------------------------------------------------------------------------------------"""


def test_hypergeometric_sampler():
    # All three draws are red.
    values = iter([0.1, 0.1, 0.1])
    assert hypergeometric_sampler(10, 4, 3, lambda: next(values)) == 3

    # First draw is blue, second is red, third is blue.
    values = iter([0.8, 0.1, 0.8])
    assert hypergeometric_sampler(10, 4, 3, lambda: next(values)) == 1

    # Zero draws means zero successes.
    assert hypergeometric_sampler(10, 4, 0, lambda: 0.5) == 0

    # No successes exist in the population.
    assert hypergeometric_sampler(10, 0, 3, lambda: 0.5) == 0


def test_hypergeometric_sampler_invalid_parameters():
    invalid_cases = [
        (0, 0, 0),  # N must be positive
        (10, -1, 3),  # K cannot be negative
        (10, 11, 3),  # K cannot exceed N
        (10, 4, -1),  # n cannot be negative
        (10, 4, 11),  # n cannot exceed N
    ]

    for N, K, n in invalid_cases:
        with pytest.raises((TypeError, ValueError)):
            hypergeometric_sampler(N, K, n, lambda: 0.5)


def test_hypergeometric_sampler_rejects_non_integer_parameters():
    invalid_cases = [
        (10.5, 4, 3),
        (10, 2.5, 3),
        (10, 4, 1.5),
        (True, 1, 1),
        (10, False, 1),
        (10, 4, True),
    ]

    for N, K, n in invalid_cases:
        with pytest.raises((TypeError, ValueError)):
            hypergeometric_sampler(N, K, n, lambda: 0.5)


@pytest.mark.parametrize("u", [-0.1, 1, 1.5, float("inf"), float("nan"), "0.5", True])
def test_hypergeometric_sampler_invalid_random_value(u):
    with pytest.raises((TypeError, ValueError)):
        hypergeometric_sampler(10, 4, 3, lambda: u)


def test_hypergeometric_simulation():
    rng = iter([0.1, 0.8, 0.1, 0.8, 0.8, 0.1])
    result = hypergeometric_simulation(2, 10, 4, 3, random_number=lambda: next(rng))

    assert result == [2, 1]


def test_hypergeometric_simulation_invalid_trials():
    with pytest.raises((TypeError, ValueError)):
        hypergeometric_simulation(0, 10, 4, 3, random_number=lambda: 0.5)


def test_hypergeometric_simulation_statistical_properties():
    rng = random.Random(42)
    hg_d = HyperGeometric(10, 4, 3)
    data = hypergeometric_simulation(10_000, 10, 4, 3, random_number=rng.random)

    assert math.isclose(empirical_mean(data), hg_d.expected_value(), abs_tol=0.05)
    assert math.isclose(empirical_variance(data), hg_d.variance(), abs_tol=0.05)

    # P(X = 2) = 0.3 for N=10, K=4, n=3.
    assert math.isclose(empirical_pmf(data, 2), hg_d.pmf(2), abs_tol=0.03)

    # P(X<=2) for N = 10, K=4, n=3
    assert math.isclose(empirical_cdf(data, 2), hg_d.cdf(2), abs_tol=0.03)
