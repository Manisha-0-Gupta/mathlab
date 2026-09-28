import math

class ExponentialDistribution:
      def __init__(self, lam):
            if not isinstance(lam, (int, float)) or lam <= 0:
                  raise ValueError("Lambda must be a positive number")
            self.lam = lam

      def pdf(self, x):
            if x < 0:
                  return 0
            return self.lam * math.exp(-self.lam * x)

      def cdf(self, x):
            if x < 0:
                  return 0
            return 1 - math.exp(-self.lam * x)

      def expected_value(self):
            return 1 / self.lam

      def variance(self):
            return 1 / (self.lam ** 2)

      def standard_deviation(self):
            return self.variance() ** 0.5