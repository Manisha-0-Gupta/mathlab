from probability.simulation import simulate


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

from probability.simulation import standard_error


def test_standard_error():
    result = standard_error((1667, 10000, 0.1667))

    assert abs(result - 0.00373) < 0.00001

    

from probability.simulation import confidence_interval


def test_confidence_interval():
    result = confidence_interval((1667, 10000, 0.1667))

    lower, upper = result

    assert abs(lower - 0.15924) < 0.00001
    assert abs(upper - 0.17416) < 0.00001