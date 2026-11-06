"""
Monte Carlo Convergence Experiment

Estimates the probability of rolling a six on a fair die
and investigates how estimator variability changes with
increasing sample sizes.
"""

import math
import random
from pathlib import Path

import matplotlib.pyplot as plt

from probability.simulations.simulation import (
    empirical_mean,
    empirical_pmf,
    sample,
    sample_variance,
)
from probability.validation import (
    check_empty_data,
    check_non_negative_integer,
    check_positive_integer,
)

# Experiment constants

THEORETICAL_P = 1 / 6
DEFAULT_SEED = 42
DEFAULT_REPETITIONS = 1000

# Documentation image directory
IMAGE_DIR = (
    Path(__file__).resolve().parents[2] / "docs" / "probability_projects" / "images"
)


def dice_sampler(rng):
    """Generate one fair six-sided die roll."""
    return rng.randint(1, 6)


def estimate_probability_of_six(n, rng):
    """Estimate the probability of rolling a six from n rolls."""

    check_positive_integer(n, "n")

    rolls = sample(lambda: dice_sampler(rng), n)

    return empirical_pmf(rolls, 6)


def repeated_estimates(n, repetitions, rng):
    """Generate repeated independent probability estimates."""
    check_positive_integer(n, "n")
    check_positive_integer(repetitions, "repetitions")

    estimates = []

    for _ in range(repetitions):
        estimates.append(estimate_probability_of_six(n, rng))

    return estimates


def analyse_estimates(estimates):
    """Calculate statistical summaries of repeated estimates."""

    if len(estimates) < 2:
        raise ValueError("At least two estimates are required")

    variance = sample_variance(estimates)
    mean = empirical_mean(estimates)

    absolute_errors = [abs(estimate - THEORETICAL_P) for estimate in estimates]

    return {
        "mean": mean,
        "variance": variance,
        "standard_deviation": math.sqrt(variance),
        "mean_absolute_error": empirical_mean(absolute_errors),
    }


def convergence_experiment(
    sample_sizes, repetitions=DEFAULT_REPETITIONS, seed=DEFAULT_SEED
):
    """Run a reproducible Monte Carlo convergence experiment."""

    check_empty_data(sample_sizes, "sample_sizes")
    check_positive_integer(repetitions, "repetitions")
    check_non_negative_integer(seed, "seed")

    rng = random.Random(seed)

    results = {}
    for sample_size in sample_sizes:
        check_positive_integer(sample_size, "sample_size")

        estimates = repeated_estimates(sample_size, repetitions, rng)

        analysis = analyse_estimates(estimates)

        analysis["theoretical_standard_error"] = math.sqrt(
            THEORETICAL_P * (1 - THEORETICAL_P) / sample_size
        )

        results[sample_size] = analysis

    return results


def plot_convergence(results):
    """Plot estimator variability and mean absolute error."""

    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    sample_sizes = sorted(results.keys())

    empirical_se = [results[n]["standard_deviation"] for n in sample_sizes]

    theoretical_se = [results[n]["theoretical_standard_error"] for n in sample_sizes]

    mean_absolute_errors = [results[n]["mean_absolute_error"] for n in sample_sizes]

    # Plot 1: Empirical SE vs theoretical SE
    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        sample_sizes,
        empirical_se,
        marker="o",
        label="Empirical SE of Estimates",
    )

    ax.plot(
        sample_sizes, theoretical_se, marker="o", linestyle="--", label="Theoretical SE"
    )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Standard Error / Theoretical Error")
    ax.set_title("Monte Carlo Convergence Estimator")
    ax.legend()
    ax.grid(True, which="both", alpha=0.3)

    fig.savefig(
        IMAGE_DIR / "monte_carlo_convergence.png",
        dpi=300,
        bbox_inches="tight",
    )

    # plot 2:- Mean Absolute error v/s sample sizes

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.plot(
        sample_sizes,
        mean_absolute_errors,
        marker="o",
        label="Mean Absolute Error",
    )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Sample Size")
    ax.set_ylabel("Mean Absolute Error")
    ax.set_title("Mean Absolute Error vs Sample Size")
    ax.legend()
    ax.grid(True, which="both", alpha=0.3)

    fig.savefig(
        IMAGE_DIR / "mean_absolute_error.png",
        dpi=300,
        bbox_inches="tight",
    )

    print(f"\nGraphs saved to: {IMAGE_DIR}")
    plt.show()


def main():
    sample_sizes = [100, 1_000, 10_000, 100_000]

    results = convergence_experiment(
        sample_sizes, repetitions=DEFAULT_REPETITIONS, seed=DEFAULT_SEED
    )

    print("\nMONTE CARLO CONVERGENCE EXPERIMENT")
    print(f"Seed: {DEFAULT_SEED}")
    print(f"Repetitions: {DEFAULT_REPETITIONS}")
    print(f"Theoretical probability: {THEORETICAL_P:.6f}")

    for sample_size, analysis in results.items():
        print(f"\nsample_size:{sample_size}")
        print(f"Mean:{analysis['mean']:.6f}")
        print(f"variance:{analysis['variance']:.8f}")
        print(f"Empirical_SE:{analysis['standard_deviation']:.6f}")
        print(f"Theoretical_SE:{analysis['theoretical_standard_error']:.6f}")
        print(f"Mean Absolute Error:{analysis['mean_absolute_error']:.6f}")

    plot_convergence(results)


if __name__ == "__main__":
    main()
