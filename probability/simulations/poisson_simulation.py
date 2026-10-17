import math

from probability.simulations.simulation import sample
from probability.validation import check_positive_integer, check_positive_real_number


def poisson_sampler(lam, random_number):
    check_positive_real_number(lam, "lam")
    if lam > 700:
        raise ValueError("lam too large for this method (use lam <= 700)")
    u = random_number()
    i = 0
    p = math.exp(-lam)
    total = p
    while total <= u:
        i += 1
        p = (p * lam) / i
        total += p

    return i


def poisson_simulation(
    trials,
    lam,
    random_number,
):
    check_positive_integer(trials, "trials")

    s = sample(lambda: poisson_sampler(lam, random_number), trials)
    return s
