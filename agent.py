"""
Abstract implementation of agent
"""


class Agent:
    def __init__(self, counties):
        self.counties = counties

    def distribute_test_kits(self):
        """
        Distribute the test kits to the counties for this agent
        :return:
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def consume_test_results(self, county, results):
        """
        Default implementation that does nothing
        :return:
        """
        return
