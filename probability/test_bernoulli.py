from probability.bernoulli import BernoulliDistribution
import math
def test_valid_probabilities():
 
      BernoulliDistribution(0)

      BernoulliDistribution(1)

      BernoulliDistribution(0.5)


def test_invalid_probabilities():

      try:
            BernoulliDistribution(2)

            assert False
      except ValueError:

            assert True

      try:
            BernoulliDistribution(-0.1)

            assert False

      except ValueError:
            
            assert True

distribution = BernoulliDistribution(0.7)
result = distribution.pmf(1)
assert math.isclose(result,0.7)

result = distribution.pmf(0)
assert math.isclose(result,0.3)

result = distribution.pmf(2)
assert result == 0


result = distribution.expected_value()
assert math.isclose(result,0.7)

result = distribution.variance()
assert math.isclose(result,0.21)

result = distribution.standard_deviation()
assert math.isclose(result,0.4582575695)

result = distribution.cdf(-1)
assert math.isclose(result,0)

result = distribution.cdf(0)
assert math.isclose(result,0.3)

result = distribution.cdf(0.5)
assert math.isclose(result,0.3)

result = distribution.cdf(1)
assert math.isclose(result,1)

result = distribution.cdf(2)
assert math.isclose(result,1)