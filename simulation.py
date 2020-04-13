from datetime import datetime
from typing import List

from county import County
from environment import Environment
from epsilon_greedy_agent import EpsilonGreedyAgent
from naive_agent import NaiveAgent
from pandas_test_kit_evaluator import PandasTestKitEvaluator
from random_test_kit_evaluator import RandomTestKitEvaluator

"""
Class that encapsulates the entirety of the simulation
"""


class Simulation:
    start_date: datetime
    end_date: datetime
    counties: List[County]
    num_test_kits_per_day = 1_000

    def __init__(self, _start_date, _end_date, _counties, _num_test_kits_per_day, _agent, _test_kit_evaluator):
        self.start_date = _start_date
        self.end_date = _end_date
        self.counties = _counties
        self.num_test_kits_per_day = _num_test_kits_per_day
        self.agent = _agent
        self.test_kit_evaluator = _test_kit_evaluator

    def run(self):
        """
        Run the simulation
        :return:
        """
        print('Running simulation with ' + str(len(self.counties)) + ' counties')
        print('start date: ' + str(self.start_date))
        print('end date: ' + str(self.end_date))

        # Initialize the environment with what we know
        environment = Environment(
            self.start_date,
            self.counties,
            self.num_test_kits_per_day,
            self.agent,
            self.test_kit_evaluator)

        # Run the simulation from start to end
        while environment.current_date < self.end_date:
            print(f'Day {environment.current_date}:')
            environment.simulate_day()


if __name__ == '__main__':

    # We can retrieve the number of tests done up to this point. Let's correlate this data with the data from the
    # following URL:

    # https://services1.arcgis.com/CY1LXxl9zlJeBuRZ/arcgis/rest/services/Florida_COVID19_Cases/FeatureServer/0/query?where=1%3D1&outFields=DATESTAMP,T_total,COUNTYNAME&returnGeometry=false&outSR=4326&f=json

    # We can use the total number of tests up to this point for a specific county to provide for a more accurate count.
    # So instead of determining the percent infected based on the population of people, determine it based on the
    # population of known tests.

    # These numbers were hand-computed
    counties = [
        County('Miami-Dade, Florida', 39077),
        County('Broward, Florida', 24451),
        County('Palm Beach, Florida', 10445),
        County('Monroe, Florida', 749),
        County('Collier, Florida', 3342)
    ]

    # The start date of the simulation
    start_date = datetime(2020, 1, 21)

    # The end date of the simulation
    end_date = datetime(2020, 4, 11)

    # The number of test kits available for distribution per-day
    num_test_kits_per_day = 100

    # Define the agent. It can either be EpsilonGreedyAgent or NaiveAgent
    agent = EpsilonGreedyAgent(counties, num_test_kits_per_day)
    # agent = NaiveAgent(counties, num_test_kits_per_day)

    # Define the test kit evaluator. It can either be RandomTestKitEvaluator or PandasTestKitEvaluator
    test_kit_evaluator = PandasTestKitEvaluator(counties)

    # What we are seeing: the number of test cases observed is

    simulation = Simulation(
        start_date,
        end_date,
        counties,
        num_test_kits_per_day,
        agent,
        test_kit_evaluator)

    simulation.run()

