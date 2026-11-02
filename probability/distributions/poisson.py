import math

from probability.utils import factorial
from probability.validation import (
    check_integer,
    check_non_negative_integer,
    check_real_number,
)


class PoissonDistribution:
    def __init__(self, lam):
        check_real_number(lam, "lam")

        if lam <= 0:
            raise ValueError("Lambda must be greater than 0")

        self.lam = lam

    def pmf(self, k):
        check_non_negative_integer(k, "k")

        return (math.exp(-self.lam) * (self.lam**k)) / factorial(k)

    def expected_value(self):
        return self.lam

    def variance(self):
        return self.lam

    def standard_deviation(self):
        return self.variance() ** 0.5

    def cdf(self, k):
        check_integer(k, "k")
        if k < 0:
            return 0

        total = 0

        for i in range(k + 1):
            total += self.pmf(i)

        return total
