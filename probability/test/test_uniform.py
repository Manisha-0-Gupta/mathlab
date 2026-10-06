from probability.uniform import UniformDistribution
import math



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