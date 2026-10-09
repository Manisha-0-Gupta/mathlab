from probability.simulations.bernoulli_simulation import bernoulli_event


def binomial_event(n, p, random_number):
    hits = 0

    for _ in range(n):
        if bernoulli_event(random_number, p) == 1:
            hits += 1

    return hits


def binomial_simulation(trials, n, p, random_number):
    observations = []

    for _ in range(trials):
        result = binomial_event(n, p, random_number)
        observations.append(result)

    return observations
