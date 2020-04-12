import pandas as pd
from result_consumer import ResultConsumer


class PandasResultConsumer(ResultConsumer):

    def __init__(self):
        self.results_frame = self.get_result_frame()

    def get_result_frame(self):
        # get dates from data in question from NYT data and store as list
        data_url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

        df = pd.read_csv(data_url, error_bad_lines=False)

        date_frame = df.groupby('date')
        dates_list = list(date_frame.groups.keys())

        # create indices for needed data
        selected_counties = ['Broward, Florida', 'Miami-Dade, Florida', 'Collier, Florida', 'Monroe, Florida',
                             'Palm Beach, Florida']

        result_frame = pd.DataFrame(index=selected_counties, columns=dates_list)

        result_frame.fillna(0, inplace=True)

        return (result_frame)

    def consume_result(self, county, date, results):
        self.results_frame.loc[county, date] = results