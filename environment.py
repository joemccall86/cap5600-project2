from datetime import datetime, timedelta
from typing import List

from agent import Agent
from epsilon_greedy_agent import EpsilonGreedyAgent
from naive_agent import NaiveAgent
from pandas_result_consumer import PandasResultConsumer
from print_result_consumer import PrintResultConsumer
from random_test_kit_evaluator import RandomTestKitEvaluator
from result_consumer import ResultConsumer
from test_kit_evaluator import TestKitEvaluator


class Environment:
    current_date: datetime
    agent: Agent
    test_kit_evaluator: TestKitEvaluator
    result_consumers: List[ResultConsumer]

    def __init__(self, current_date, counties, num_test_kits_per_day):
        self.current_date = current_date
        self.counties = counties
        self.agent = EpsilonGreedyAgent(self.counties, num_test_kits_per_day)
        # self.agent = NaiveAgent(self.counties, num_test_kits_per_day)
        self.test_kit_evaluator = RandomTestKitEvaluator(self.current_date)
        self.result_consumers = [PrintResultConsumer(), PandasResultConsumer(), self.agent]

        # Tell the agent to distribute the test kits before the first day is simulated so every county starts with some
        # test kits.
        self.agent.distribute_test_kits()

    def simulate_day(self):
        """
        Simulate a single day of the simulation.
        :return:
        """
        for county in self.counties:

            # Perform the tests
            county.perform_tests(self.test_kit_evaluator)

            # Get the test results
            results = county.report_results()

            # Consume the test results
            for consumer in self.result_consumers:
                consumer.consume_result(county, self.current_date, results)

            # Tell the agent to distribute the test kits
            self.agent.distribute_test_kits()

        # Advance the day
        self.current_date = self.current_date + timedelta(days=1)
        self.test_kit_evaluator.current_date = self.current_date
