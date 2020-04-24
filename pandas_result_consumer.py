"""
/**
 * Implementation of a result consumer that stores the data locally in a Pandas dataframe, to be used later for evaluation
 * 
 * @author Joe McCall; Chris Zahuranec
 * @date 4/24/2020
 * @info Course CAP5600
 */
"""
from typing import List

import pandas as pd

from county import County
from result_consumer import ResultConsumer


class PandasResultConsumer(ResultConsumer):

    counties: List[County]

    measured_results_key = 'Measured Positive Cases (P_m)'

    def __init__(self, _counties):
        """
        Default constructor
        """
        self.counties = _counties
        self.results_frame = self.get_result_frame()

    def get_result_frame(self):
        """
        :return: the pandas result frame attached to this consumer
        """
        # get dates from data in question from NYT data and store as list
        data_url = 'us-counties.csv'
        # data_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

        df = pd.read_csv(data_url, error_bad_lines=False)

        date_frame = df.groupby('date')
        dates_list = list(date_frame.groups.keys())

        # create indices for needed data
        selected_counties = [c.name for c in self.counties]

        result_frame = pd.DataFrame(index=selected_counties, columns=dates_list)

        result_frame.fillna(0, inplace=True)

        # result_frame.loc['Area Total'] = result_frame.sum()

        return (result_frame)

    def consume_result(self, county, date, results):
        """
        Consume the result of a test kit
        :param county: the county that's tested
        :param date: the date of the test
        :param results: the number of positive cases that day
        :return:
        """
        date_string = date.strftime('%Y-%m-%d')
        self.results_frame.loc[county.name, date_string] = results

    def return_total(self):
        """
        :return: the computed total frame attached to this result consumer
        """
        self.results_frame.loc[self.measured_results_key] = self.results_frame.sum()
        self.results_frame = self.results_frame.loc[self.measured_results_key]
        return self.results_frame