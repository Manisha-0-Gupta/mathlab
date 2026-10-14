class UniformDistribution:
    def __init__(self, a, b):
        if (
            isinstance(a, bool)
            or isinstance(b, bool)
            or not isinstance(a, (int, float))
            or not isinstance(b, (int, float))
        ):
            raise TypeError("a,b must be an integer or a floating number")

        if a >= b:
            raise ValueError("a must be less than b")

        self.a = a
        self.b = b

    def pdf(self, x):
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError("x must be an integer or a floating number")
        if not self.a <= x <= self.b:
            return 0

        return 1 / (self.b - self.a)

    def interval_probability(self, c, d):

        if (
            isinstance(c, bool)
            or isinstance(d, bool)
            or not isinstance(c, (int, float))
            or not isinstance(d, (int, float))
        ):
            raise TypeError("c,d must be an integer or a floating number")

        if c > d:
            raise ValueError("c must be less than or equal to d")

        return (max(0, min(d, self.b) - max(c, self.a))) / (self.b - self.a)

    def cdf(self, k):
        if isinstance(k, bool) or not isinstance(k, (int, float)):
            raise TypeError("k must be an integer or a floating number")
        if k < self.a:
            return 0
        elif k > self.b:
            return 1

        return (k - self.a) / (self.b - self.a)

    def expected_value(self):
        return (self.a + self.b) / 2

    def variance(self):
        return ((self.b - self.a) ** 2) / 12

    def standard_deviation(self):
        return self.variance() ** 0.5
