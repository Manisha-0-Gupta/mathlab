from probability.negative_binomial import NegativeBinomial
import math


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
      except ValueError:
            assert True

      try:
            distribution.pmf(1.5)
            assert False
      except ValueError:
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
      except ValueError:
            assert True