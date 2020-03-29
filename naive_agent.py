"""
Implementation of an agent that evenly distributes test kits evenly to all counties
"""
from agent import Agent


class NaiveAgent(Agent):
    test_kit_capacity = 0

    def __init__(self, counties, test_kit_capacity):
        super().__init__(counties)
        self.test_kit_capacity = test_kit_capacity

    def distribute_test_kits(self):
        """
        Distribute the test kits evenly to all counties
        :return:
        """
        num_test_kits_each = self.test_kit_capacity / len(self.counties)
        for county in self.counties:
            county.receive_test_kits(num_test_kits_each)
