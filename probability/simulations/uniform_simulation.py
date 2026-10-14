from probability.simulations.simulation import (
    sample,
    simulate,
)


def uniform_sampler(a, b, random_number):
    if not a < b:
        raise ValueError("a must be less than b")

    u = random_number()

    return a + u * (b - a)


def uniform_simulation(trials, a, b, random_number):
    if not isinstance(trials, int) or isinstance(trials, bool) or trials <= 0:
        raise ValueError("Trials must be greater than zero")

    data = sample(lambda: uniform_sampler(a, b, random_number), trials)

    return data


def interval_event(a, b, c, d, random_number):
    if (
        isinstance(c, bool)
        or isinstance(d, bool)
        or not isinstance(c, (int, float))
        or not isinstance(d, (int, float))
    ):
        raise TypeError("c,d must be an integer or a floating number")
    if c > d:
        raise ValueError("c must be less than or equal to  d")

    sampler = uniform_sampler(a, b, random_number)

    return c <= sampler <= d


def probability_of_an_interval(trials, a, b, c, d, random_number):
    if (
        isinstance(c, bool)
        or isinstance(d, bool)
        or not isinstance(c, (int, float))
        or not isinstance(d, (int, float))
    ):
        raise TypeError("c,d must be an integer or a floating number")
    if c > d:
        raise ValueError("c must be less than or equal to  d")

    hits, trials, probability = simulate(
        trials, lambda: interval_event(a, b, c, d, random_number)
    )
    return hits, trials, probability
