from datetime import datetime
from typing import List

from county import County
from environment import Environment
from epsilon_greedy_agent import EpsilonGreedyAgent
from naive_agent import NaiveAgent
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

    # The counties we want to simulation. County population information gathered from Wikipedia.
    counties = [
        County('Miami-Dade, Florida', 2_761_581),
        County('Broward, Florida', 1_951_260),
        County('Palm Beach, Florida', 1_485_941),
        County('Monroe, Florida', 75_027),
        County('Collier, Florida', 378_488)
    ]

    # The start date of the simulation
    start_date = datetime(2020, 1, 1)

    # The end date of the simulation
    end_date = datetime(2020, 3, 23)

    # The number of test kits available for distribution per-day
    num_test_kits_per_day = 1_000

    # Define the agent. It can either be EpsilonGreedyAgent or NaiveAgent
    agent = EpsilonGreedyAgent(counties, num_test_kits_per_day)
    # agent = NaiveAgent(counties, num_test_kits_per_day)

    # Define the test kit evaluator. It can either be RandomTestKitEvaluator or PandasTestKitEvaluator
    test_kit_evaluator = RandomTestKitEvaluator()

    simulation = Simulation(
        start_date,
        end_date,
        counties,
        num_test_kits_per_day,
        agent,
        test_kit_evaluator)

    simulation.run()
