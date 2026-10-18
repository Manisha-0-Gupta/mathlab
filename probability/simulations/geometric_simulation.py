"""
Geometric Distribution

Models the number of independent Bernoulli trials required to obtain the first success.
Parameter:
    p: Probability of success per trial, where 0 < p <= 1.

"""

from probability.simulations.simulation import sample, simulate
from probability.validation import (
    check_positive_integer,
    check_probability_value,
    check_random_value,
    check_real_number,
)


def check_p(p):
    check_real_number(p, "p")
    check_probability_value(p, "p")
    if p == 0:
        raise ValueError("p can not be zero for geometric distribution")


def geometric_sampler(p, random_number):
    check_p(p)
    count = 0
    while True:
        u = random_number()
        check_random_value(u)
        count += 1
        if u < p:
            return count


def geometric_simulation(trials, p, random_number):
    check_positive_integer(trials, "trials")
    check_p(p)
    s = sample(lambda: geometric_sampler(p, random_number), trials)
    return s


def success_at_first_or_third_try(p, random_number):
    check_p(p)
    g = geometric_sampler(p, random_number)
    return g == 1 or g == 3


def probability_of_success_at_first_or_third_try(trials, p, random_number):
    check_positive_integer(trials, "trials")
    check_p(p)
    hits, trials, estimated_probability = simulate(
        trials, lambda: success_at_first_or_third_try(p, random_number)
    )

    return hits, trials, estimated_probability
