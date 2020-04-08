from random import random

from agent import Agent


class EpsilonGreedyAgent(Agent):

    epsilon = 0.5

    def __init__(self, counties, test_kit_capacity):
        super().__init__(counties, test_kit_capacity)

        self.county_cases = dict.fromkeys(counties, 0)
        self.trial_count = 0
        self.highest_county = self.counties[0]

    def distribute_test_kits(self):
        # Treat each test kit as a "trial" for the purposes of classical epsilon-greedy.
        # Start out with 0 test kits for each county
        test_kit_map = dict.fromkeys(self.counties, 0)

        # Determine which county gets the test kit
        for test_kit_num in range(0, self.test_kit_capacity):
            if test_kit_num % 2 == 0:
                # Exploitation strategy: give the test kit to county with the highest number of positive results
                test_kit_map[self.highest_county] += 1
            else:
                # Exploration strategy: this test kit goes to a random county
                random_county = random.choice(self.counties)
                test_kit_map[random_county] += 1

        # Distribute the test kits based on the internal map
        for county in self.counties:
            county.receive_test_kits(test_kit_map[county])


    def consume_result(self, county, date, results):
        """
        Update the results in our in-memory store
        :param county: the county
        :param date: the date (ignored by this implementation)
        :param results: the number of positive cases
        :return:
        """
        self.county_cases[county] += results

        # Update the highest county
        for county in self.counties:
            if self.county_cases[county] > self.county_cases[self.highest_county]:
                self.highest_county = county

