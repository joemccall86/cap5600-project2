"""
/**
 * Represents a county in this simulation. Each county is responsible for running their own tests,
 * keeping track of the number of test kits they have, and reporting back the results.
 * 
 * @author Joe McCall; Chris Zahuranec
 * @date 4/24/2020
 * @info Course CAP5600
 */
"""
from scoring_strategy import ScoringStrategy


class County:
    name = ''
    num_test_kits = 0
    population = 0
    num_measured_positive_cases = 0
    num_measured_negative_cases = 0
    num_actual_positive_cases = 0
    score = 0

    def __init__(self, name, population):
        """
        Constructor for the county
        """
        self.name = name
        self.population = population

    def perform_tests(self, test_kit_evaluator, current_date):
        """
        Run all the test kits, updating the number of positive cases and number of test kits remaining
        :return:
        """
        test_kit_evaluator.update_county_data(self, current_date)
        for _ in range(self.num_test_kits):
            self.perform_test(test_kit_evaluator, current_date)

        # We have used up all the test kits, so set the number to 0
        self.num_test_kits = 0

        # Update the score for this county thus far
        self.score += ScoringStrategy.compute_score(self)

    def perform_test(self, test_kit_evaluator, current_date):
        """
        Run a single test
        :return: True if this test resulted in a positive result, False otherwise
        """

        positive = test_kit_evaluator.evaluate_test(self, current_date)
        if positive:
            self.num_measured_positive_cases += 1

        return positive

    def receive_test_kits(self, num_test_kits):
        """
        Receive test kits
        :param num_test_kits: the number of test kits to receive
        :return:
        """
        # print(f'{self.name} received {num_test_kits} test kits for a total of {self.num_test_kits}')
        self.num_test_kits += num_test_kits

    def report_results(self):
        """
        Report the number of positive cases in this county
        :return: the number of positive cases in this county
        """
        return self.num_measured_positive_cases
