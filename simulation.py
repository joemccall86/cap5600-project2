from datetime import datetime
from typing import List

import requests

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
            self.agent,
            self.test_kit_evaluator)

        # Run the simulation from start to end
        while environment.current_date < self.end_date:
            print(f'Day {environment.current_date}:')
            environment.simulate_day()

        # Print the score
        print(f'The score for agent {type(agent)} is {environment.compute_score()}')


def build_counties(county_names_in, state_in):
    """
    Build the counties in Florida based on the data from Florida's DOH data
    See https://open-fdoh.hub.arcgis.com/datasets/florida-covid19-cases-by-county
    :param county_names_in: the list of counties to check
    :return: the built list of county objects and their "populations" based on the number of total tests.
    """
    built_counties = []

    # Grab the data from the Florida DOH API
    raw_request = requests.get(
        'https://services1.arcgis.com/CY1LXxl9zlJeBuRZ/arcgis/rest/services/Florida_COVID19_Cases/FeatureServer/0'
        '/query?where=1%3D1&outFields=DATESTAMP,T_total,COUNTYNAME&returnGeometry=false&outSR=4326&f=json')

    # Filter it to just the cases list
    cases_list = raw_request.json()["features"]

    # Build out the list of counties
    for county_name in county_names_in:
        matching_counties = list(filter(lambda x: x['attributes']['COUNTYNAME'] == county_name.upper(), cases_list))

        # Fail fast if this response does not contain one of the counties we're looking for
        if len(matching_counties) == 0:
            raise 'County with name ' + county_name + ' not found in json'

        # Based on the data grab the total number of tests to this point
        num_tests = int(matching_counties[0]['attributes']['T_total'])

        full_county_name = county_name + ', ' + state_in
        county = County(full_county_name, num_tests)
        built_counties.append(county)

        # Print out for debugging purposes
        print('Testing County ' + county.name + ', ' + str(county.population))

    return built_counties


if __name__ == '__main__':

    county_names = [
        'Miami-Dade',
        'Broward',
        'Palm Beach',
        'Monroe',
        'Collier'
    ]

    counties = build_counties(county_names, 'Florida')

    # The start date of the simulation
    start_date = datetime(2020, 1, 21)

    # The end date of the simulation
    end_date = datetime(2020, 4, 18)

    # The number of test kits available for distribution per-day
    num_test_kits_per_day = 100

    # Define the agent. It can either be EpsilonGreedyAgent or NaiveAgent
    # agent = EpsilonGreedyAgent(counties, num_test_kits_per_day)
    agent = NaiveAgent(counties, num_test_kits_per_day)


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

