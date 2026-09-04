def validate_distribution(variables, probabilities):
    if len(variables) != len(probabilities):
        return False

    if abs(sum(probabilities) -1) > 1e-9:
        return False

    for value in probabilities:
        if value < 0:
            return False

    return True


def expected_value(variables, probabilities):
    if not validate_distribution(variables, probabilities):
        raise ValueError("Invalid probability distribution")

    total = 0

    for i in range(len(variables)):
        total += variables[i] * probabilities[i]

    return total


def variance(variables, probabilities):
    total = 0
    expected_value_squared = expected_value(variables, probabilities) ** 2

    for i in range(len(variables)):
        total += (variables[i] ** 2) * probabilities[i]

    return total - expected_value_squared


def standard_deviation(variables, probabilities):
    return variance(variables, probabilities) ** 0.5

def event_probability(variables,probabilities,event):
    if not validate_distribution(variables,probabilities):
        raise ValueError("Invalid probability distribution")
    total = 0
    for i in range(len(variables)):
        if variables[i] in event:
            total += probabilities[i]
    return total

def complement_probability(variables,probabilities,event):
    return 1 - event_probability(variables,probabilities,event)
