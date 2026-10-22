"""
Hypergeometric Distribution Simulation
======================================

Overview
--------
Simulates the number of successes in a fixed number of draws from a finite
population without replacement.

Parameters
----------
N : int
    Total population size, N >= 1.
K : int
    Number of successes in the population, 0 <= K <= N.
n : int
    Number of draws, 0 <= n <= N.

Sampling Algorithm
------------------
For each draw:
1. Calculate the probability of success using red_left / total_left.
2. Generate a random number in [0, 1).
3. If the random number is below the success probability, increment the
   success count and decrement red_left.
4. Decrement total_left regardless of the outcome.
5. Return the total number of successes after n draws.

Complexity
----------
Time: O(n), where n is the number of draws.
Auxiliary space: O(1).


Applications
------------
- Quality control and defect sampling
- Ecological population sampling
- Card-drawing probability
- Survey sampling from finite populations

Note:- random_number is a function imported from probability.simulations.simulation
"""

from probability.simulations.simulation import sample
from probability.validation import (
    check_non_negative_integer,
    check_positive_integer,
    check_random_value,
)


def check_parameters(N, K, n):
    check_positive_integer(N, "N")
    check_non_negative_integer(K, "K")
    if not K <= N:
        raise ValueError("K must be 0 <= K <= N")
    check_non_negative_integer(n, "n")
    if not n <= N:
        raise ValueError("n must be 0 <= n <= N")


def hypergeometric_sampler(N, K, n, random_number):
    check_parameters(N, K, n)
    red_balls = K
    total_left = N
    count = 0

    for _ in range(n):
        u = random_number()
        check_random_value(u, "u")
        if u < red_balls / total_left:
            count += 1
            red_balls -= 1

        total_left -= 1

    return count


def hypergeometric_simulation(trials, N, K, n, random_number):
    check_positive_integer(trials, "trials")
    check_parameters(N, K, n)

    s = sample(lambda: hypergeometric_sampler(N, K, n, random_number), trials)

    return s
