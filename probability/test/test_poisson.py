import math
import random

import pytest

from probability.poisson import PoissonDistribution
from probability.simulations.poisson_simulation import (
    poisson_sampler,
    poisson_simulation,
)
from probability.simulations.simulation import (
    empirical_cdf,
    empirical_mean,
    empirical_pmf,
    empirical_variance,
)


def test_valid_lam():

    PoissonDistribution(3)


def test_invalid_lam():

    try:
        PoissonDistribution(0)
        assert False
    except ValueError:
        assert True

    try:
        PoissonDistribution(-1)
        assert False
    except ValueError:
        assert True


def test_pmf():
    distribution = PoissonDistribution(3)
    try:
        distribution.pmf(-1)
        assert False
    except ValueError:
        assert True

    try:
        distribution.pmf(1.5)
        assert False
    except TypeError:
        assert True

    assert math.isclose(distribution.pmf(0), 0.049787068367863944)
    assert math.isclose(distribution.pmf(1), 0.14936120510359183)
    assert math.isclose(distribution.pmf(3), 0.22404180765538775)


def test_statistics():
    distribution = PoissonDistribution(3)

    assert math.isclose(distribution.expected_value(), 3)
    assert math.isclose(distribution.variance(), 3)
    assert math.isclose(distribution.standard_deviation(), 3**0.5)


def test_cdf():
    distribution = PoissonDistribution(3)

    try:
        distribution.cdf(1.5)
        assert False
    except TypeError:
        assert True

    assert math.isclose(distribution.cdf(0), 0.049787068367863944)
    assert math.isclose(distribution.cdf(1), 0.19914827347145578)
    assert math.isclose(distribution.cdf(3), 0.6472318887822313)


# ------------------------------------------------------------------------

"""TEST-POISSON-SIMULATION"""


def test_poisson_sampler_returns_correct_count():
    result = poisson_sampler(2, lambda: 0.5)
    assert result == 2


def test_poisson_sampler_invalid_lam():
    with pytest.raises(ValueError):
        poisson_sampler(0, lambda: 0.5)

    with pytest.raises(ValueError):
        poisson_sampler(-1, lambda: 0.5)

    with pytest.raises(ValueError):
        poisson_sampler(float("inf"), lambda: 0.5)

    with pytest.raises(TypeError):
        poisson_sampler("2", lambda: 0.5)


def test_poisson_sampler_rejects_lam_above_limit():
    with pytest.raises(ValueError, match="lam too large"):
        poisson_sampler(701, lambda: 0.5)


def test_poisson_sampler_accepts_lam_at_upper_limit():
    result = poisson_sampler(700, lambda: 0.5)
    assert isinstance(result, int)
    assert result >= 0


def test_poisson_sampler_returns_zero_when_u_below_first_probability():
    result = poisson_sampler(2, lambda: 0.1)
    assert result == 0


def test_poisson_sampler_returns_one():
    result = poisson_sampler(2, lambda: 0.2)
    assert result == 1


def test_poisson_simulation_returns_requested_number_of_observations():
    result = poisson_simulation(5, 2, lambda: 0.5)
    assert len(result) == 5


def test_poisson_simulation_returns_non_negative_integer_counts():
    result = poisson_simulation(10, 2, lambda: 0.5)
    assert all(isinstance(x, int) and x >= 0 for x in result)


def test_poisson_simulation_rejects_invalid_trials():
    with pytest.raises(ValueError):
        poisson_simulation(0, 2, lambda: 0.5)


def test_statistical_calculation():
    rng = random.Random(42)
    p_d = PoissonDistribution(2)
    data = poisson_simulation(10_000, 2, rng.random)

    assert math.isclose(p_d.expected_value(), empirical_mean(data), abs_tol=0.05)
    assert math.isclose(p_d.variance(), empirical_variance(data), abs_tol=0.05)
    assert math.isclose(p_d.cdf(3), empirical_cdf(data, 3), abs_tol=0.05)
    assert math.isclose(p_d.pmf(3), empirical_pmf(data, 3), abs_tol=0.05)
