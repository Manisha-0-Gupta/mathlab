class GeometricDistribution:

      def __init__(self,p):

            if not 0 < p <=1:
                  raise ValueError("Invalid value of probability")

            self.p = p

      def pmf(self,k):

            if not isinstance(k,int) or k <= 0:
                  raise ValueError("K should be a positive non-zero integer")

            return ((1-self.p)**(k-1))*self.p

      def expected_value(self):
            return 1/self.p

      def variance(self):
            return (1-self.p)/(self.p**2)

      def standard_deviation(self):
            return self.variance()**0.5

      def cdf(self,k):
            if not isinstance(k,int):
                  raise ValueError("K should be an integer")

            if k <=0:
                  return 0

            return 1-((1-self.p)**k)
      

            