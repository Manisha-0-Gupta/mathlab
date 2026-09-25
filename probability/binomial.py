from probability.utils import factorial

class BinomialDistribution:

      def __init__(self,n,p):
            if not isinstance(n,int) or n <0:
                  raise ValueError("Number of trials must be non-negative integer")

            if not 0<=p<=1:
                  raise ValueError("Invalid probability value")

            self.n = n
            self.p = p

      def expected_value(self):
            return self.n*self.p

      def variance(self):
            return self.n*(self.p)*(1-self.p)

      def standard_deviation(self):
            return self.variance()**0.5


      def pmf(self,k):

            if k <0 or k >self.n:
                  raise ValueError("Invalid value of k")
            
            combination = (factorial(self.n))/((factorial(k)*(factorial(self.n-k))))

            return combination*((self.p)**k)*((1-self.p)**(self.n-k))

      def cdf(self,k):
            
            if k <0 :
                  return 0
            
            elif k>self.n:
                  return 1
            
            cdf_total = 0

            for i in range(k+1):

                  cdf_total += self.pmf(i)

            return cdf_total


      
       
            
                  
            
            
