from probability.binomial import BinomialDistribution
import math

def test_valid_n_p():
      BinomialDistribution(10,0.7)
      BinomialDistribution(1,0.5)

def test_invalid_n_p():
      try:
            BinomialDistribution(2.5,0.7)
            assert False
      except ValueError:
            assert True
      try:
            BinomialDistribution(-1,0.5)
            assert False
      except ValueError:
            assert True

      try:
            BinomialDistribution(10,-1)
            assert False
      except ValueError:
            assert True

      try:
            BinomialDistribution(10,2)
            assert False
      except ValueError:
             assert True


distribution = BinomialDistribution(10,0.7)


def test_expected_value():
      assert math.isclose(distribution.expected_value(),7)

def test_variance():
      assert math.isclose(distribution.variance(),2.1)

def test_standard_deviation():
      assert math.isclose(distribution.standard_deviation(),1.44913767462)

def test_pmf():

            assert math.isclose(distribution.pmf(7),0.266827932)
            assert math.isclose(distribution.pmf(0), 0.3**10)
            assert math.isclose(distribution.pmf(10), 0.7**10)

            try:
                   distribution.pmf(-1)
                   assert False
            except ValueError:
                   assert True

            try:
                   distribution.pmf(11)
                   assert False
            except ValueError:
                   assert True

def test_pmf_sum_to_one():
      total = 0

      for k in range(distribution.n+1):
            total += distribution.pmf(k)

      assert math.isclose(total,1)

def test_cdf():

      assert math.isclose(distribution.cdf(-1),0)
      assert math.isclose(distribution.cdf(0),0.3**10)
      assert math.isclose(distribution.cdf(2),distribution.pmf(0)+distribution.pmf(1)+distribution.pmf(2))
      assert math.isclose(distribution.cdf(11),1)
      assert math.isclose(distribution.cdf(10),1)


# TEST-BINOMIAL-SIMULATION

from probability.simulations.binomial_simulation import (binomial_event,binomial_simulation,empirical_mean,empirical_variance)

def test_binomial_event_success():

      assert binomial_event(5,0.5,lambda:0.3) == 5

def test_binomial_event_failure():
      assert binomial_event(5,0.5,lambda:0.8) == 0

def test_binomial_event():
      values = iter([0.2,0.3,0.4,0.5,0.6,0.7,0.8])
      assert binomial_event(7,0.5,lambda: next(values)) == 3

def test_binomial_simulation():
      value = iter([0.1,0.2,0.3,0.5,0.6,
                  0.3,0.4,0.7,0.5,0.8,
                  0.4,0.8,0.9,0.7,0.6,            
      ])

      assert binomial_simulation(3,5,0.5,lambda:next(value)) == [3,2,1]
simulation_distribution = BinomialDistribution(10,0.3)
import math
import random

data = binomial_simulation(10_000,10,0.3,random.random)

def test_empirical_mean():
      assert math.isclose(
            empirical_mean(data),
            simulation_distribution.expected_value(),
            abs_tol=0.05
      )

def test_empirical_variance():
      assert math.isclose(
            empirical_variance(data),
            simulation_distribution.variance(),
            abs_tol=0.05
      )
