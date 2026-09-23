class BernoulliDistribution:

      def __init__(self,p):

            if not 0<= p <=1:
                  raise ValueError ("Invalid value")

            self.p = p

      def pmf(self,x):
            if x ==1:
                  probability = self.p
            elif x == 0:
                  probability = 1-self.p
            else:
                  probability = 0
            return probability

      def expected_value(self):
            return self.p
      
      def variance(self):
            return self.p*(1-self.p)

      def standard_deviation(self):
            return self.variance()**0.5

      def cdf(self,x):
            if x <0:
                  probability = 0
            elif 0<=x<1:
                  probability = 1-self.p
            elif x>= 1:
                  probability = 1
            return probability
      