from probability.simulations.bernoulli_simulation import bernoulli_event
from probability.simulations.simulation import random_number

def binomial_event(n,p,random_number):
      hits = 0

      for _ in range(n):
            if bernoulli_event(random_number,p) ==1:
                  hits +=1

      return hits

def binomial_simulation(trials,n,p,random_number):
      observations = []

      for _ in range(trials):
            result = binomial_event(n,p,random_number)
            observations.append(result)

      return observations

data = binomial_simulation(10_000,10,0.3,random_number)

def empirical_mean(data):

      return sum(data)/len(data)

def empirical_variance(data):
      total = 0
      mean = empirical_mean(data)
      for i in range(len(data)):
            total += (data[i] - mean)**2

      return total/len(data)



