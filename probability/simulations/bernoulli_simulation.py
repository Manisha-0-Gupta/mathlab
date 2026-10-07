from probability.simulations.simulation import (random_number,estimate_probability,standard_error,confidence_interval)


def bernoulli_event(random_number,p):
      if random_number() < p:
            return 1
      return 0

def bernoulli_simulation(trials,p,random_number):
      hits = 0

      for _ in range(trials):
            
            hits += bernoulli_event(random_number,p)
            
      estimated_probability = estimate_probability(hits,trials)

      std_error = standard_error(estimated_probability,trials)

      confidence_interval_ = confidence_interval(estimated_probability,std_error)

      result =  {'Trials':trials,
              'Total_hits':hits,
              'Given_probability':p,
              'Estimated_probability':estimated_probability,
              'Standard_error':std_error,
              'Confidence_interval':confidence_interval_
              }
      
      return result

def repeated_simulation(experiments,trials,p,random_number):
      data = {}

      for i in range(1,experiments+1):
            data[i] = bernoulli_simulation(trials,p,random_number)

      return data
      

def ci_coverage(experiments,trials,p,random_number):
      hits = 0
      data = repeated_simulation(experiments,trials,p,random_number)

      for i in range(1,experiments+1):
            if data[i]['Confidence_interval'][0] <= p <= data[i]['Confidence_interval'][1]:
                  hits +=1

      result = hits/experiments

      return result 


