import random
# Random Number between 0 to 1

def random_number():
      return random.random()


# Experiment functions

def roll_the_dice():
    return random.randint(1, 6)

def even_die():
    result = roll_the_dice()
    return result%2 ==0




# Simulation engine


def simulate(trials,experiment):
    success_count = 0

    for _ in range(trials):
            if experiment():
                 success_count += 1

    probability = success_count/trials
      
    return success_count,trials,probability


# Statistical Calculation

def estimate_probability(hits,trials):
      return hits/trials


def standard_error(probability,trials):
      return ((probability*(1-probability))/trials)**0.5


def confidence_interval(probability,std_error):

    lower_bound = probability - 1.96*std_error
    upper_bound = probability + 1.96*std_error

    return [lower_bound,upper_bound]




