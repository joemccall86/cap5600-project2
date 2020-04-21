from random import random
from typing import List

import pandas as pd

from county import County
from test_kit_evaluator import TestKitEvaluator


class PandasTestKitEvaluator(TestKitEvaluator):

    counties: List[County]
    actual_positive_cases_key = 'Actual Positive Cases (P_a)'

    def __init__(self, counties):
        self.counties = counties
        self.data_frame = self.get_data_frame()

    def get_data_frame(self):

        data_url = 'us-counties.csv'
        # data_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

        df = pd.read_csv(data_url, error_bad_lines=False)

        # create 'areas', county + state

        df['Area'] = df['county'] + ', ' + df['state']

        # obtain primary keys of areas available in data

        area_df = df.groupby('Area')
        areas_list = list(area_df.groups.keys())

        # obtain available dates in data

        date_frame = df.groupby('date')
        dates_list = list(date_frame.groups.keys())

        # create 'infection frame' that can hold data in format needed

        infection_frame = pd.DataFrame(index=areas_list, columns=dates_list)

        # filter frame for counties in question
        selected_counties = [c.name for c in self.counties]
        final_frame = infection_frame.loc[selected_counties]

        # fill the final frame for use compared to available data
        for location in selected_counties:
            for time in dates_list:
                target = df[(df['Area'] == location) & (df['date'] == time)]
                if not target.empty:
                    insert_value = target.iloc[0]['cases']
                    final_frame.at[location, time] = insert_value

        # replace 'NaN' data points as 0's
        final_frame.fillna(0, inplace=True)

        #add row for totals used to generate graph
        final_frame.loc[self.actual_positive_cases_key] = final_frame.sum()

        return final_frame

    def return_final_counts(self):

        self.final_total = self.data_frame.loc[self.actual_positive_cases_key]

        return self.final_total

    def update_county_data(self, county, current_date):
        """
        Evaluate the county's chances of returning a positive result based on the data stored by Pandas and the
        current date.
        :param county: the county to check
        :param current_date: the date to check for
        :return:
        """
        date_string = current_date.strftime('%Y-%m-%d')
        #converted_date = '2020-01-21'
        infected_population = self.data_frame.loc[county.name, date_string]

        # Update the actual positive cases on the county object from real data
        county.num_actual_positive_cases = infected_population

    def evaluate_test(self, county, current_date):
        """
        Evaluate the county's chances of returning a positive result based on the data stored by Pandas and the
        current date.
        :param county: the county to check
        :param current_date: the date to check for
        :return:
        """
        infection_percent = county.num_actual_positive_cases / county.population
        chance = random()
        result = False
        if chance < infection_percent:
            result = True

        return result
