import random

"""
Represents a county in this simulation. Each county is responsible for running their own tests,
keeping track of the number of test kits they have, and reporting back the results.
"""


class County:
    name = ''
    num_test_kits = 0
    population = 0
    num_positive_cases = 0

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def perform_tests(self):
        """
        Run all the test kits, updating the number of positive cases and number of test kits remaining
        :return:
        """
        for _ in range(self.num_test_kits):
            self.perform_test()

        # We have used up all the test kits, so set the number to 0
        self.num_test_kits = 0

    def perform_test(self):
        """
        Run a single test
        :return: True if this test resulted in a positive result, False otherwise
        """
        # NOTE: on my other workstation I have a test implementation code that I'd like to use. For the time being let's make this just a random
        # coin-flip. 50/50. That way we have at least _something_ running for this test.
        coin_flip = random.randint(0, 1)
        positive = coin_flip == 1  # TODO fill in with test evaluator implementation
        if positive:
            self.num_positive_cases += 1

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
        return self.num_positive_cases
