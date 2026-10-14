import math
import random

import pytest

from probability.simulations.simulation import (
    confidence_interval,
    empirical_cdf,
    empirical_mean,
    empirical_pmf,
    empirical_variance,
    standard_error,
)
from probability.simulations.uniform_simulation import (
    interval_event,
    probability_of_an_interval,
    uniform_sampler,
    uniform_simulation,
)
from probability.uniform import UniformDistribution


def test_valid_interval():
    UniformDistribution(0, 10)
    UniformDistribution(10, 30)


def test_invalid_interval():
    try:
        UniformDistribution(10, 10)
        assert False
    except ValueError:
        assert True

    try:
        UniformDistribution(20, 10)
        assert False
    except ValueError:
        assert True


def test_pdf():
    distribution = UniformDistribution(10, 30)

    assert math.isclose(distribution.pdf(10), 1 / 20)
    assert math.isclose(distribution.pdf(15), 1 / 20)
    assert math.isclose(distribution.pdf(30), 1 / 20)

    assert distribution.pdf(5) == 0
    assert distribution.pdf(35) == 0


def test_cdf():
    distribution = UniformDistribution(10, 30)

    assert distribution.cdf(5) == 0
    assert math.isclose(distribution.cdf(10), 0)
    assert math.isclose(distribution.cdf(15), 0.25)
    assert math.isclose(distribution.cdf(20), 0.5)
    assert math.isclose(distribution.cdf(30), 1)
    assert distribution.cdf(35) == 1


def test_statistics():
    distribution = UniformDistribution(10, 30)

    assert math.isclose(distribution.expected_value(), 20)
    assert math.isclose(distribution.variance(), 33.333333333333336)
    assert math.isclose(distribution.standard_deviation(), 5.773502691896258)


def test_interval_probability():
    distribution = UniformDistribution(2, 8)
    assert math.isclose(distribution.interval_probability(3, 5), 1 / 3)
    assert math.isclose(distribution.interval_probability(1, 5), 1 / 2)
    assert math.isclose(distribution.interval_probability(6, 10), 1 / 3)
    assert math.isclose(distribution.interval_probability(9, 10), 0)
    assert math.isclose(distribution.interval_probability(2, 8), 1)
    assert math.isclose(distribution.interval_probability(4, 4), 0)


"""
-----------------------------------------------------------------------------------------
"""
# TEST-UNIFORM-DISTRIBUTION-SIMULATION


def test_uniform_sampler():

    assert uniform_sampler(2, 8, lambda: 0.25) == 3.5
    assert uniform_sampler(2, 8, lambda: 0) == 2


def test_invalid_parameters():

    with pytest.raises(ValueError):
        uniform_sampler(8, 6, lambda: 0.25)
    with pytest.raises(ValueError):
        uniform_sampler(2, 2, lambda: 0.25)


def test_uniform_simulation_trials():

    with pytest.raises(ValueError):
        uniform_simulation(2.5, 2, 8, lambda: 0.25)
    with pytest.raises(ValueError):
        uniform_simulation(True, 2, 8, lambda: 0.25)
    with pytest.raises(ValueError):
        uniform_simulation(-100, 2, 8, lambda: 0.25)


def test_uniform_simulation():
    values = iter([0.1, 0.7, 0.3, 0.5, 0.6, 0.3, 0.4])
    result = uniform_simulation(7, 2, 8, lambda: next(values))

    assert result == pytest.approx(
        [
            2.6,
            6.2,
            3.8,
            5,
            5.6,
            3.8,
            4.4,
        ]
    )


def test_interval_event():
    assert interval_event(2, 8, 3, 5, lambda: 0.4) is True
    assert interval_event(2, 8, 3, 5, lambda: 0.1) is False
    assert interval_event(2, 8, 3, 5, lambda: 0.6) is False


def test_probability_of_an_interval():
    u_d = UniformDistribution(2, 8)
    _, __, probability = probability_of_an_interval(
        10000, 2, 8, 3, 5, random.Random(42).random
    )
    assert math.isclose(probability, u_d.interval_probability(3, 5), abs_tol=0.05)


def test_invalid_parameters_probability_of_an_interval():
    with pytest.raises(TypeError):
        probability_of_an_interval(10, 2, 8, True, 5, lambda: 0.25)
    with pytest.raises(TypeError):
        probability_of_an_interval(10, 2, 8, 3, False, lambda: 0.25)
    with pytest.raises(ValueError):
        probability_of_an_interval(10, 2, 8, 7, 5, lambda: 0.25)


def test_empirical_mean():
    rng = random.Random(42)
    u_d = UniformDistribution(2, 8)
    data = uniform_simulation(10_000, 2, 8, rng.random)
    assert math.isclose(u_d.expected_value(), empirical_mean(data), abs_tol=0.05)


def test_empirical_variance():
    rng = random.Random(42)
    u_d = UniformDistribution(2, 8)
    data = uniform_simulation(10_000, 2, 8, rng.random)

    assert math.isclose(u_d.variance(), empirical_variance(data), abs_tol=0.05)


def test_empirical_cdf():
    rng = random.Random(42)
    u_d = UniformDistribution(2, 8)
    data = uniform_simulation(10_000, 2, 8, rng.random)
    assert math.isclose(u_d.cdf(5), empirical_cdf(data, 5), abs_tol=0.05)
