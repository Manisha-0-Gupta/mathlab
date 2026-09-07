import random

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


def standard_error(simulation_result):

    hit,trials,probability = simulation_result

    return ((probability*(1-probability))/trials)**0.5


def confidence_interval(simulation_result):

    _,__,probability = simulation_result
    se = standard_error(simulation_result)

    lower_bound = probability - 2*se
    upper_bound = probability + 2*se

    return lower_bound,upper_bound



