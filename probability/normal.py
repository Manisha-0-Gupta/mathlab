import math

class NormalDistribution:

      def __init__(self,mu,sigma):
            if not sigma >0:
                  raise ValueError("Sigma should be a positive value")

            self.mu = mu
            self.sigma = sigma

      def pdf(self,x):
            a = math.exp(-((x-self.mu)**2/(2*self.sigma**2)))
            b = self.sigma*(2*math.pi)**0.5
            return a/b

      def cdf(self,x):
            steps = 10000

            lower = self.mu-8*self.sigma
            upper = self.mu+8*self.sigma

            if x<=lower:
                  return 0
            if x >= upper:
                  return 1

            width = (x-lower)/steps
            total = 0

            for i in range(steps):
                  left = lower + i * width
                  right = left + width

                  total += ((self.pdf(left)+self.pdf(right))/2) * width

            return total 

      def expected_value(self):
            return self.mu

      def variance(self):
            return self.sigma**2

      def  standard_deviation(self):
            return self.sigma
      