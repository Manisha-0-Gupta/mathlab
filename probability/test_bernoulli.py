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


# TEST-BERNOULLI-SIMULATION
from probability.simulate_bernoulli import (bernoulli_event,bernoulli_simulation,ci_coverage,repeated_simulation)

def test_bernoulli_event_success():
      assert bernoulli_event(0.3,0.7) == 1

def test_bernoulli_event_failure():
      assert bernoulli_event(0.8,0.7) == 0

def test_bernoulli_simulation_success():
      result = bernoulli_simulation(10,0.7,lambda:0.3)

      assert result['Trials'] == 10
      assert result['Total_hits'] == 10

def test_bernoulli_simulation_failure():
      result = bernoulli_simulation(10, 0.5, lambda: 0.8)
      assert result['Trials'] == 10
      assert result['Total_hits'] == 0

def test_repeated_simulation():
      data = repeated_simulation(
        5,
        10,
        0.5,
        lambda: 0.3
      )

      assert len(data) == 5

      for i in range(1, 6):
            assert data[i]['Trials'] == 10
            assert data[i]['Total_hits'] == 10

def test_ci_coverage():
      values = iter([0.3, 0.8] * 5)

      result = ci_coverage(
            experiments=5,
            trials=2,
            p=0.5,
            random_number=lambda: next(values)
            )

      assert math.isclose(result, 1.0)      