import math

from probability.gamma import GammaDistribution


def test_valid_parameters():

    GammaDistribution(1, 2)
    GammaDistribution(5, 2)
    GammaDistribution(2.5, 1)


def test_invalid_parameters():
    for alpha, lam in [(0, 1), (-1, 1), (1, 0), (1, -1), (-2, -3)]:
        try:
            GammaDistribution(alpha, lam)
            assert False
        except ValueError:
            pass


def test_pdf():
    d = GammaDistribution(1, 2)

    # Gamma(1, lambda) = Exponential(lambda)
    assert math.isclose(d.pdf(0), 2)
    assert math.isclose(d.pdf(1), 2 * math.exp(-2))


def test_statistics():
    d = GammaDistribution(5, 2)

    assert math.isclose(d.expected_value(), 2.5)
    assert math.isclose(d.variance(), 1.25)
    assert math.isclose(d.standard_deviation(), math.sqrt(1.25))


def test_exponential_special_case():
    gamma = GammaDistribution(1, 2)

    assert math.isclose(gamma.pdf(1), 2 * math.exp(-2))


def test_cdf():
    d = GammaDistribution(1, 2)

    # Gamma(1, 2) is Exponential(2)
    assert math.isclose(d.cdf(1), 1 - math.exp(-2), rel_tol=1e-5)


def test_cdf_boundaries():
    d = GammaDistribution(5, 2)

    assert d.cdf(-1) == 0
    assert d.cdf(0) == 0


def test_fractional_alpha_pdf():
    d = GammaDistribution(0.5, 2)

    assert math.isclose(d.pdf(1), math.sqrt(2 / math.pi) * math.exp(-2), rel_tol=1e-9)
