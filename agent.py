"""
/**
 * Abstract class that consumes the results from a test cit for a specific county
 * 
 * @author Joe McCall; Chris Zahuranec
 * @date 4/24/2020
 * @info Course CAP5600
 */
"""
from result_consumer import ResultConsumer


class Agent(ResultConsumer):
    test_kit_capacity = 0

    def __init__(self, counties, test_kit_capacity):
        """
        Constructor for the agent
        """
        self.counties = counties
        self.test_kit_capacity = test_kit_capacity

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
