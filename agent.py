"""
Abstract implementation of agent
"""
from result_consumer import ResultConsumer


class Agent(ResultConsumer):
    def __init__(self, counties):
        self.counties = counties

    def distribute_test_kits(self):
        """
        Distribute the test kits to the counties for this agent
        :return:
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def consume_result(self, county, date, results):
        """
        Default implementation that does nothing
        :return:
        """
        return
