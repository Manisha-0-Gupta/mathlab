from probability.geometric import GeometricDistribution
import math

from probability.geometric import GeometricDistribution


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
      assert math.isclose(distribution.variance(), 0.3 / (0.7 ** 2))


def test_standard_deviation():
      expected = (0.3 / (0.7 ** 2)) ** 0.5
      assert math.isclose(distribution.standard_deviation(), expected)

def test_cdf():
      distribution = GeometricDistribution(0.7)

      assert math.isclose(distribution.cdf(1), 0.7)
      assert math.isclose(distribution.cdf(3), 0.973)
      assert math.isclose(distribution.cdf(5), 0.99757)
      assert distribution.cdf(0) == 0