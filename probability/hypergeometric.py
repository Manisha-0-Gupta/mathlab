from probability.utils import factorial

class HyperGeometric:

      def __init__(self,N,K,n):

            if not isinstance(N,int) or N <=0:
                  raise ValueError("N should be a positive integer greater than zero")

            if not isinstance(K,int) or not 0<= K <= N:
                  raise ValueError("Invalid value of K")

            if not isinstance(n,int) or not 0<= n <= N:
                  raise ValueError("Invalid value of n")

            self.N = N
            self.K = K
            self.n = n

      def pmf(self,k):

            if not isinstance(k,int):
                  raise ValueError("k should be an integer")

            if not max(0,self.n-(self.N-self.K))<= k <= min(self.n,self.K):
                  raise ValueError("Value of k is out of bounds")
            
            fav_selection1 =( factorial(self.K) ) / ( factorial(self.K-k) * factorial(k) )
            fav_selection2 = ( factorial(self.N-self.K) ) / ( factorial(self.N-self.K-self.n+k) * factorial(self.n-k))
            total_combination = factorial(self.N) / ( factorial(self.N-self.n) * factorial(self.n) )

            return (fav_selection1*fav_selection2)/total_combination

      def expected_value(self):
            return (self.n*self.K)/self.N

      def variance(self):
            if self.N  ==1:
                  return 0 
            a = self.expected_value()
            b = 1-(self.K/self.N)
            c = (self.N-self.n)/(self.N -1)
            return a*b*c

      def standard_deviation(self):
            return self.variance()**0.5

      def cdf(self,k):
            if not isinstance(k,int):
                  raise ValueError("k should be an integer")
            if k < max(0, self.n - (self.N-self.K)):
                  return 0
            if k > min(self.n,self.K):
                  return 1

            total = 0

            for i in range(max(0,self.n-(self.N-self.K)),k+1):
                  total += self.pmf(i)

            return total 