import math

from probability.hypergeometric import HyperGeometric


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
