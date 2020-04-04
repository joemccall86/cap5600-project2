from datetime import datetime
from typing import List

from county import County
from environment import Environment

"""
Class that encapsulates the entirety of the simulation
"""


class Simulation:
    start_date: datetime
    end_date: datetime
    counties: List[County]
    num_test_kits_per_day = 1_000

    def __init__(self, start_date, end_date, counties):
        self.start_date = start_date
        self.end_date = end_date
        self.counties = counties

    def run(self):
        """
        Run the simulation
        :return:
        """
        print('Running simulation with ' + str(len(self.counties)) + ' counties')
        print('start date: ' + str(self.start_date))
        print('end date: ' + str(self.end_date))

        # Initialize the environment with what we know
        environment = Environment(self.start_date, self.counties, self.num_test_kits_per_day)

        # Run the simulation from start to end
        while environment.current_date < self.end_date:
            print(f'Day {environment.current_date}:')
            environment.simulate_day()


if __name__ == '__main__':
    # TODO read this information from a configuration file, or from the command line arguments

    # Placeholder counties for now
    miami_dade = County('Miami-Dade', 2_761_581)
    broward = County('Broward', 1_951_260)
    palm_beach = County('Palm Beach', 1_485_941)
    monroe = County('Monroe', 75_027)
    collier = County('Collier', 378_488)

    simulation = Simulation(datetime(2020, 1, 1), datetime(2020, 3, 23), [
        miami_dade,
        broward,
        palm_beach,
        monroe,
        collier
    ])

    simulation.run()
