from experiments.probability_projects.monte_carlo_convergence import (
    convergence_experiment,
)

results_1 = convergence_experiment(
    [100, 1000, 10000, 100000], repetitions=1000, seed=42
)

results_2 = convergence_experiment(
    [100, 1000, 10000, 100000], repetitions=1000, seed=42
)

assert results_1 == results_2

print("Reproducibility test passed.")
