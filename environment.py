from datetime import datetime, timedelta
from typing import List

from agent import Agent
from pandas_result_consumer import PandasResultConsumer
from print_result_consumer import PrintResultConsumer
from result_consumer import ResultConsumer
from test_kit_evaluator import TestKitEvaluator


class Environment:
    current_date: datetime
    agent: Agent
    test_kit_evaluator: TestKitEvaluator
    result_consumers: List[ResultConsumer]

    def __init__(self, current_date, counties, agent, test_kit_evaluator):
        self.current_date = current_date
        self.counties = counties
        self.agent = agent
        self.test_kit_evaluator = test_kit_evaluator
        self.pandas_consumer = PandasResultConsumer(self.counties)
        self.result_consumers = [PrintResultConsumer(), self.pandas_consumer, self.agent]

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
            county.perform_tests(self.test_kit_evaluator, self.current_date)

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

    def compute_score(self):
        """
        Compute the score based on the number of actual minus the number of measured positive cases, summed from every
        day.
        :return: The score for this environment
        """

        score = 0
        for county in self.counties:
            score += county.score

        return score
