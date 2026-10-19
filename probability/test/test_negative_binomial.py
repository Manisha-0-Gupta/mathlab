import math
import random

import pytest

from probability.negative_binomial import NegativeBinomial
from probability.simulations.negative_binomial_simulation import (
    negative_binomial_sampler,
    negative_binomial_simulation,
)
from probability.simulations.simulation import (
    empirical_cdf,
    empirical_mean,
    empirical_pmf,
    empirical_variance,
)


def test_valid_parameters():
    NegativeBinomial(1, 0.5)
    NegativeBinomial(2, 0.7)
    NegativeBinomial(10, 0.2)


def test_invalid_probability():
    try:
        NegativeBinomial(2, 0)
        assert False
    except ValueError:
        assert True

    try:
        NegativeBinomial(2, -0.1)
        assert False
    except ValueError:
        assert True

    try:
        NegativeBinomial(2, 1.1)
        assert False
    except ValueError:
        assert True


def test_invalid_r():
    try:
        NegativeBinomial(0, 0.5)
        assert False
    except ValueError:
        assert True

    try:
        NegativeBinomial(-1, 0.5)
        assert False
    except ValueError:
        assert True

    try:
        NegativeBinomial(2.5, 0.5)
        assert False
    except ValueError:
        assert True


def test_pmf():
    distribution = NegativeBinomial(2, 0.5)

    assert math.isclose(distribution.pmf(2), 0.25)

    assert math.isclose(distribution.pmf(3), 0.25)

    assert math.isclose(distribution.pmf(5), 0.125)


def test_invalid_k():
    distribution = NegativeBinomial(2, 0.5)

    try:
        distribution.pmf(1)
        assert False
    except TypeError:
        assert True

    try:
        distribution.pmf(1.5)
        assert False
    except TypeError:
        assert True


def test_statistics():
    distribution = NegativeBinomial(2, 0.5)

    assert math.isclose(distribution.expected_value(), 4)
    assert math.isclose(distribution.variance(), 4)
    assert math.isclose(distribution.standard_deviation(), 2)


def test_cdf():
    distribution = NegativeBinomial(2, 0.5)

    assert math.isclose(distribution.cdf(1), 0)
    assert math.isclose(distribution.cdf(2), 0.25)
    assert math.isclose(distribution.cdf(3), 0.50)
    assert math.isclose(distribution.cdf(5), 0.8125)


def test_invalid_cdf_k():
    distribution = NegativeBinomial(2, 0.5)

    try:
        distribution.cdf(2.5)
        assert False
    except TypeError:
        assert True


"""------------------------------------------------------------------------------------------------------"""
"""TEST-NEGATIVE-BINOMIAL-SIMULATION"""
"""------------------------------------------------------------------------------------------------------"""


def test_negative_binomial_sampler():
    # All successes on the first r trials
    values = iter([0.1, 0.2, 0.3])
    assert negative_binomial_sampler(3, 0.5, lambda: next(values)) == 3

    # Successes after failures
    values = iter([0.8, 0.2, 0.7, 0.1])
    assert negative_binomial_sampler(2, 0.5, lambda: next(values)) == 4

    # Invalid r
    with pytest.raises(ValueError):
        negative_binomial_sampler(0, 0.5, lambda: 0.1)

    # Invalid p
    with pytest.raises(ValueError):
        negative_binomial_sampler(2, 0, lambda: 0.1)

    # Invalid random value
    with pytest.raises(ValueError):
        negative_binomial_sampler(2, 0.5, lambda: 2)


def test_negative_binomial_simulation():
    # Invalid trials
    with pytest.raises(ValueError):
        negative_binomial_simulation(0, 2, 0.5, lambda: 0.1)

    # Returns the requested number of observations
    data = negative_binomial_simulation(5, 2, 0.5, lambda: 0.1)
    assert len(data) == 5

    # Every observation is at least r
    assert all(value >= 2 for value in data)


def test_negative_binomial_statistical_calculation():
    rng = random.Random(42)
    r = 3
    p = 0.5

    distribution = NegativeBinomial(r, p)
    data = negative_binomial_simulation(10_000, r, p, rng.random)
    # empirical mean
    assert math.isclose(
        distribution.expected_value(),
        empirical_mean(data),
        abs_tol=0.05,
    )
    # empirical variance
    assert math.isclose(
        distribution.variance(),
        empirical_variance(data),
        abs_tol=0.05,
    )
    # Empirical PMF: probability of exactly 4 trials
    assert math.isclose(
        distribution.pmf(4),
        empirical_pmf(data, 4),
        abs_tol=0.03,
    )

    # Empirical CDF: probability of at most 4 trials
    assert math.isclose(
        distribution.cdf(4),
        empirical_cdf(data, 4),
        abs_tol=0.03,
    )
