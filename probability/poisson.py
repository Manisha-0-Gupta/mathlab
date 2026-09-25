from probability.utils import factorial

import math


class PoissonDistribution:

      def __init__(self, lam):
            if lam <= 0:
                  raise ValueError("Lambda must be greater than 0")

            self.lam = lam

      def pmf(self, k):
            if not isinstance(k, int) or k < 0:
                  raise ValueError("K should be non negative integer")

            return (math.exp(-self.lam) * (self.lam ** k)) / factorial(k)

      def expected_value(self):
             return self.lam

      def variance(self):
             return self.lam

      def standard_deviation(self):
            return self.variance() ** 0.5

      def cdf(self,k):
            if not isinstance(k,int):
                  raise ValueError("K should be an integer")

            if k <0:
                  return 0

            total = 0

            for i in range(k+1):
                  total += self.pmf(i)

            return total
      
