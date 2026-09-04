import math
from probability.probability import expected_value
from probability.probability import variance
from probability.probability import standard_deviation
from probability.probability import event_probability
from probability.probability import complement_probability

result = expected_value([-1,2],[0.5,0.5])

assert result ==0.5

result = expected_value([0,10],[0.9,0.1])

assert result == 1

result = variance([-1,2],[0.5,0.5])

assert result == 2.25

result = standard_deviation([-1,2],[0.5,0.5])

assert result == 1.5

try:
      expected_value([1,2],[0.3,0.3])
      assert False
except ValueError:
      assert True  

try:
      expected_value([1,2],[-0.5,0.5])
      assert False
except ValueError:
      assert True    

result = expected_value([1, 2, 3], [0.1, 0.2, 0.7])
assert math.isclose(result,2.6)


result = event_probability([1, 2, 3, 4, 5, 6],
                           [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
                           [2, 4, 6])

assert result == 0.5

try:
    event_probability([1, 2], [0.3, 0.3], [1])
    assert False
except ValueError:
    assert True

result = complement_probability([1, 2, 3, 4, 5, 6],
                           [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
                           [2, 4, 6])
assert result == 0.5