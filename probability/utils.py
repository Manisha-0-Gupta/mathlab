import math


def factorial(n):
    total = 1
    for num in range(1, n + 1):
        total *= num
    return total


def gamma_function(x):

    if x <= 0:
        raise ValueError("x must be positive")

    if isinstance(x, int):
        return factorial(x - 1)

    g = 7
    z = x - 1
    t = z + g + 0.5
    coefficients = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7,
    ]

    a = (2 * math.pi) ** 0.5

    b = t ** (z + 0.5) * math.exp(-t)

    total = coefficients[0]

    for i in range(1, len(coefficients)):
        total += coefficients[i] / (z + i)

    c = total

    return a * b * c


def beta_function(alpha, beta):

    if alpha <= 0 or beta <= 0:
        raise ValueError("Alpha and beta must be greater than zero")

    return (gamma_function(alpha) * gamma_function(beta)) / gamma_function(alpha + beta)
