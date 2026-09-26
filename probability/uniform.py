class UniformDistribution:

      def __init__(self,a,b):

            if a >= b:
                  raise ValueError("a must be less than b")

            self.a = a
            self.b = b

      def pdf(self,x):
            if not self.a <= x <= self.b:
                  return 0

            return 1/(self.b-self.a)

      def cdf(self,k):
            if k< self.a:
                  return 0
            elif k> self.b:
                  return 1

            return (k-self.a)/(self.b-self.a)

      def expected_value(self):
            return (self.a+self.b)/2

      def variance(self):
            return ((self.b-self.a)**2)/12

      def standard_deviation(self):
            return self.variance()**0.5

