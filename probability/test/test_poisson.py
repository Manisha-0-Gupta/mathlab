from probability.poisson import PoissonDistribution
import math

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
      except ValueError:
            assert True

      assert math.isclose(distribution.pmf(0),0.049787068367863944)
      assert math.isclose(distribution.pmf(1),0.14936120510359183)
      assert math.isclose(distribution.pmf(3),0.22404180765538775)


def test_statistics():
      distribution = PoissonDistribution(3)

      assert math.isclose(distribution.expected_value(),3)
      assert math.isclose(distribution.variance(),3)
      assert math.isclose(distribution.standard_deviation(),3**0.5)

def test_cdf():
      distribution = PoissonDistribution(3)

      try:
            distribution.cdf(1.5)
            assert False
      except ValueError:
            assert True

      assert math.isclose(distribution.cdf(0), 0.049787068367863944)
      assert math.isclose(distribution.cdf(1), 0.19914827347145578)
      assert math.isclose(distribution.cdf(3), 0.6472318887822313)



   