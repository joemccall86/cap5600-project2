from datetime import datetime, timedelta

from agent import Agent
from naive_agent import NaiveAgent


class Environment:
    current_date: datetime
    agent: Agent

    def __init__(self, current_date, counties, num_test_kits_per_day):
        self.current_date = current_date
        self.counties = counties
        self.agent = NaiveAgent(self.counties, num_test_kits_per_day)

        # Tell the agent to distribute the test kits before the first day is simulated so every county starts with some test kits.
        self.agent.distribute_test_kits()

    def simulate_day(self):
        """
        Simulate a single day of the simulation.
        :return:
        """
        for county in self.counties:

            # Perform the tests
            county.perform_tests()

            # Get the test results
            results = county.report_results()  # TODO do something with this

            print(f"results for county {county.name}: {results}")

            # Have our agent consume them
            self.agent.consume_test_results(county, results)

            # Tell the agent to distribute the test kits
            self.agent.distribute_test_kits()

        # Advance the day
        self.current_date = self.current_date + timedelta(days=1)
