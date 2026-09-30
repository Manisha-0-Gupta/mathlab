from probability.utils import beta_function
import math

class BetaDistribution:

      def __init__(self,alpha,beta):
            if alpha <=0 or beta <=0:
                  raise ValueError("Alpha and beta must be greater than zero")

            self.alpha = alpha
            self.beta = beta

      def pdf(self,x):
            if x <0 or x >1:
                  return 0

            a = x**(self.alpha-1) * (1-x)**(self.beta-1)
            b = beta_function(self.alpha,self.beta)

            return a/b

      def expected_value(self):
            return self.alpha/(self.alpha+self.beta)

      def variance(self):
            return (
                  (self.alpha*self.beta) /
                  (
                        ((self.alpha+self.beta)**2) *
                  (self.alpha+self.beta+1)
                  )
            )

      def standard_deviation(self):
            return self.variance()**0.5

      def cdf(self,x):
            if x <= 0:
                  return 0
            if x >= 1:
                  return 1

            steps = 10000
            width = x/steps

            total = 0
            for i in range(steps):
                  left = i*width
                  right = left+width

                  total +=(
                        (self.pdf(left)+self.pdf(right))/2
                  ) * width

            return total
