from random import random

from agent import Agent


class EpsilonGreedyAgent(Agent):
    # Epsilon value that shows how much exploration is favored over exploitation.
    # A value of 1 will always distribute the test kits evenly
    # A value of 0 will always give all of the test kits to the county with the most positive cases the previous day
    epsilon = 0.5

    def __init__(self, counties, test_kit_capacity):
        super().__init__(counties, test_kit_capacity)

        self.county_cases = dict.fromkeys(counties, 0)
        self.trial_count = 0
        self.highest_county = self.counties[0]

    def distribute_test_kits(self):
        # The top county receives (1-epsilon) * test_kit_capacity test kits (Exploitation phase)
        exploitation_kits = (1 - self.epsilon) * self.test_kit_capacity

        # The remaining kits are distributed evenly among the remaining counties (Exploration phase)
        exploration_kits = self.test_kit_capacity - exploitation_kits
        exploration_kits_per_county = exploration_kits / (len(self.counties) - 1)

        # Distribute the test kits based on the internal map
        for county in self.counties:
            if county == self.highest_county:
                county.receive_test_kits(int(exploitation_kits))
            else:
                county.receive_test_kits(int(exploration_kits_per_county))

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
