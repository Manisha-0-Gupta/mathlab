from probability.simulations.simulation import simulate
import math

def always_success():
      return True

def always_failure():
      return False

def test_simulate_all_sucess():

      result = simulate(100,always_success)

      assert result == (100,100,1.0)

def test_simulate_all_failure():

      result = simulate(100,always_failure)

      assert result == (0,100,0.0)

from probability.simulations.simulation import (estimate_probability,standard_error,confidence_interval)

def test_estimate_probability():
      assert math.isclose(estimate_probability(70,100),0.7)

def test_standard_error():
      assert math.isclose(standard_error(0.7,100),0.045825756949558406)

def test_confidence_interval():
      result = confidence_interval(0.5,0.05)
      lower = result[0]
      upper = result[1]
      assert math.isclose(lower,0.402)
      assert math.isclose(upper,0.598)
