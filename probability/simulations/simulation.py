import random

# Random Number between 0 to 1


def random_number():
    return random.random()


# sample


def sample(sampler, n):
    """
    Draw n values from a sampler.

    sampler: a function that returns one random value each time it is called.
    Returns a list of n values.
    """
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n must be nonzero positive integer")

    values = []

    for _ in range(n):
        values.append(sampler())

    return values


# Simulation engine


def simulate(trials, experiment):
    """
    Run a yes/no experiment many times.

    experiment: a function that returns True (success) or False.
    Returns (successes, trials, estimated probability).

    """
    if not isinstance(trials, int) or isinstance(trials, bool) or trials <= 0:
        raise ValueError("Trials must be nonzero positive integer")

    successes = 0

    for _ in range(trials):
        if experiment():
            successes += 1

    return successes, trials, estimate_probability(successes, trials)


# Statistical Calculation


def estimate_probability(hits, trials):
    return hits / trials


def standard_error(probability, trials):
    return ((probability * (1 - probability)) / trials) ** 0.5


def confidence_interval(probability, std_error):

    lower_bound = probability - 1.96 * std_error
    upper_bound = probability + 1.96 * std_error

    return [lower_bound, upper_bound]


def empirical_mean(data):
    if len(data) == 0:
        raise ZeroDivisionError("Data is empty")

    return sum(data) / len(data)


def empirical_variance(data):
    if len(data) == 0:
        raise ValueError("Data must not be empty")
    total = 0
    mean = empirical_mean(data)
    for i in range(len(data)):
        total += (data[i] - mean) ** 2

    return total / len(data)


def standard_error_of_mean(data):
    if len(data) == 0:
        raise ValueError("Data must not be empty")
    standard_deviation = empirical_variance(data) ** 0.5
    return standard_deviation / (len(data) ** 0.5)


def empirical_pmf(data, k):
    if len(data) == 0:
        raise ValueError("Data must not be empty")
    hit = 0
    for value in data:
        if value == k:
            hit += 1

    return hit / len(data)


def empirical_cdf(data, k):
    if len(data) == 0:
        raise ValueError("Data must not be empty")
    hit = 0
    for value in data:
        if value <= k:
            hit += 1

    return hit / len(data)
