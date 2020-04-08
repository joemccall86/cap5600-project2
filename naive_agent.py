from agent import Agent

"""
Implementation of an agent that evenly distributes test kits evenly to all counties
"""


class NaiveAgent(Agent):

    def __init__(self, counties, test_kit_capacity):
        super().__init__(counties, test_kit_capacity)

    def distribute_test_kits(self):
        """
        Distribute the test kits evenly to all counties
        :return:
        """
        num_test_kits_each = int(self.test_kit_capacity / len(self.counties))
        for county in self.counties:
            county.receive_test_kits(num_test_kits_each)
