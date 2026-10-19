"""
Negative Binomial Distribution

Models the number of independent Bernoulli trials required to obtain r successes.
Parameters:
    r: Required number of successes, where r >= 1.
    p: Probability of success per trial, where 0 < p <= 1.

"""

from probability.simulations.simulation import sample
from probability.validation import (
    check_positive_integer,
    check_probability_value,
    check_random_value,
)


def check_p(p):
    check_probability_value(p, "p")
    if p == 0:
        raise ValueError("for negative binomial distribution p can not be zero")


def negative_binomial_sampler(r, p, random_number):
    check_positive_integer(r, "r")
    check_p(p)
    count = 0
    success_count = 0
    while success_count < r:
        u = random_number()
        check_random_value(u)
        if u < p:
            success_count += 1
        else:
            count += 1

    return count + success_count


def negative_binomial_simulation(trials, r, p, random_number):
    check_positive_integer(trials, "trials")
    s = sample(lambda: negative_binomial_sampler(r, p, random_number), trials)
    return s
