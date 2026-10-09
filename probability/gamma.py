import math

from probability.utils import gamma_function


class GammaDistribution:
    def __init__(self, alpha, lam):

        if alpha <= 0 or lam <= 0:
            raise ValueError("Alpha and lambda must be greater than zero ")

        self.alpha = alpha
        self.lam = lam

    def pdf(self, x):

        if x < 0:
            return 0

        a = (self.lam**self.alpha) * x ** (self.alpha - 1) * math.exp(-self.lam * x)

        b = gamma_function(self.alpha)

        return a / b

    def expected_value(self):
        return self.alpha / self.lam

    def variance(self):
        return self.alpha / ((self.lam) ** 2)

    def standard_deviation(self):
        return self.variance() ** 0.5

    def cdf(self, x):

        if x <= 0:
            return 0

        steps = 10000
        width = x / steps

        total = 0

        for i in range(steps):
            left = i * width
            right = left + width

            total += ((self.pdf(left) + self.pdf(right)) / 2) * width

        return total
