from random import random

import pandas as pd
from test_kit_evaluator import TestKitEvaluator


class PandasTestKitEvaluator(TestKitEvaluator):

    def __init__(self):
        self.data_frame = self.get_data_frame()

    def get_data_frame(self):

        data_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

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

        selected_counties = ['Broward, Florida', 'Miami-Dade, Florida', 'Collier, Florida', 'Monroe, Florida',
                             'Palm Beach, Florida']
        final_frame = infection_frame.loc[selected_counties]

        # fill the final frame for use compared to available data
        for location in selected_counties:
            for time in dates_list:
                target = df[(df['Area'] == location) & (df['date'] == time)]
                if target.empty == False:
                    insert_value = target.iloc[0]['cases']
                    final_frame.at[location, time] = insert_value

        # replace 'NaN' data points as 0's
        final_frame.fillna(0, inplace=True)

        return final_frame

    def evaluate_test(self, county, current_date):
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
        infection_percent = infected_population / county.population
        chance = random()
        result = False
        if chance < infection_percent:
            result = True

        return result
