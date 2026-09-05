
class ProbabilityDistribution:

    def __init__(self,distribution):
        self.distribution = distribution

        probabilities = self.distribution.values()

        if any(probability < 0 for probability in probabilities):
            raise ValueError("Probabilities can not be negative")

        if abs(sum(probabilities) -1) > 1e-9:
            raise ValueError("Probabilities must sum to 1")

    def expected_value(self):
        total = 0
        for variables,probability in self.distribution.items():
            total += variables*probability
        return total

    def variance(self):
        total = 0
        expected_value_squared = self.expected_value() ** 2

        for variable,probability in self.distribution.items():
            total += (variable ** 2) * probability

        return total - expected_value_squared

    def standard_deviation(self):
        return self.variance()**0.5

    def event_probability(self,event):

        total = 0

        for variables,probability in self.distribution.items():

            if variables in event:
                total +=probability

        return total

    def complement_probability(self,event):

        return 1 - self.event_probability(event)

    def conditional_probability(self,a,b):

        common = [x for x in a if x in b]

        common_probability = self.event_probability(common)

        probability_of_b = self.event_probability(b)

        if probability_of_b == 0:
            raise ZeroDivisionError("Probability of B is zero ")
        
        return common_probability/probability_of_b