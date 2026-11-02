from probability.utils import factorial


class NegativeBinomial:
    def __init__(self, r, p):

        if not 0 < p <= 1:
            raise ValueError("Invalid value of p")
        if not isinstance(r, int) or r <= 0:
            raise ValueError("r must be positive integer greater than 1")

        self.r = r
        self.p = p

    def pmf(self, k):
        if not isinstance(k, int) or k < self.r:
            raise TypeError("Invalid value of k")

        binomial_coeff = factorial(k - 1) / (
            factorial(k - self.r) * factorial(self.r - 1)
        )

        return binomial_coeff * (1 - self.p) ** (k - self.r) * self.p**self.r

    def expected_value(self):
        return self.r * (1 / self.p)

    def variance(self):
        return (self.r * (1 - self.p)) / (self.p) ** 2

    def standard_deviation(self):
        return self.variance() ** 0.5

    def cdf(self, k):
        if not isinstance(k, int):
            raise TypeError("k must be an integer")

        if k < self.r:
            return 0

        total = 0

        for i in range(self.r, k + 1):
            total += self.pmf(i)

        return total
