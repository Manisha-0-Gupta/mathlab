import math

from probability.exponential import ExponentialDistribution


def test_valid_parameters():
    ExponentialDistribution(2)
    ExponentialDistribution(0.5)
    ExponentialDistribution(10)


def test_invalid_parameters():
    for value in [0, -1, -0.5, "2"]:
        try:
            ExponentialDistribution(value)
            assert False
        except ValueError:
            pass


def test_pdf():
    d = ExponentialDistribution(2)

    assert math.isclose(d.pdf(-1), 0)
    assert math.isclose(d.pdf(0), 2)
    assert math.isclose(d.pdf(1), 2 * math.exp(-2))


def test_cdf():
    d = ExponentialDistribution(2)

    assert math.isclose(d.cdf(-1), 0)
    assert math.isclose(d.cdf(0), 0)
    assert math.isclose(d.cdf(1), 1 - math.exp(-2))


def test_statistics():
    d = ExponentialDistribution(2)

    assert math.isclose(d.expected_value(), 0.5)
    assert math.isclose(d.variance(), 0.25)
    assert math.isclose(d.standard_deviation(), 0.5)


def test_cdf_approaches_one():
    d = ExponentialDistribution(2)

    assert d.cdf(10) > 0.999


def test_pdf_decreases():
    d = ExponentialDistribution(2)

    assert d.pdf(1) > d.pdf(2) > d.pdf(3)
