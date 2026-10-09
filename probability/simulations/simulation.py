import random

# Random Number between 0 to 1


def random_number():
    return random.random()


# Simulation engine


def simulate(trials, experiment):
    success_count = 0

    for _ in range(trials):
        if experiment():
            success_count += 1

    probability = success_count / trials

    return success_count, trials, probability


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

    return sum(data) / len(data)


def empirical_variance(data):
    total = 0
    mean = empirical_mean(data)
    for i in range(len(data)):
        total += (data[i] - mean) ** 2

    return total / len(data)


def standard_error_of_mean(data):
    standard_deviation = empirical_variance(data) ** 0.5
    return standard_deviation / (len(data) ** 0.5)


def empirical_pmf(data, k):
    hit = 0
    for value in data:
        if value == k:
            hit += 1

    return hit / len(data)


def empirical_cdf(data, k):

    hit = 0
    for value in data:
        if value <= k:
            hit += 1

    return hit / len(data)
