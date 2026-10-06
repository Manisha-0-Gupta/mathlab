import math
from probability.probability import ProbabilityDistribution

try:
    distribution = ProbabilityDistribution({1:0.2,2:-0.8})
    assert False
except ValueError:
    assert True

try:
    distribution = ProbabilityDistribution({1:0.2,2:0.2})
    assert False
except ValueError:
    assert True

distribution = ProbabilityDistribution({
    1: 0.2,
    2: 0.5,
    3: 0.3
})

result = distribution.expected_value()

assert math.isclose(result , 2.1)

distribution = ProbabilityDistribution({
    -1: 0.5,
    2: 0.5
})
result = distribution.variance()

assert math.isclose(result, 2.25)

result = distribution.standard_deviation()

assert math.isclose(result,1.5)

distribution = ProbabilityDistribution({
    1: 1/6,
    2: 1/6,
    3: 1/6,
    4: 1/6,
    5: 1/6,
    6: 1/6
})

result = distribution.event_probability([2,4,6])

assert math.isclose(result,1/2)

result = distribution.complement_probability([2,4,6])

assert math.isclose(result,1/2)

result = distribution.conditional_probability([4,6],[4,5,6])

assert math.isclose(result,2/3)

try:
    distribution = ProbabilityDistribution({1:0.5,-1:0.5,2:0})
    distribution.conditional_probability([1],[2])
    assert False
except ZeroDivisionError:
    assert True