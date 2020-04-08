from result_consumer import ResultConsumer


class PandasResultConsumer(ResultConsumer):
    def consume_result(self, county, date, results):
        # TODO fill this in
        # We need to store the data in a dataframe that will be used at the end to build a graph.
        # The data frame should store the following data:
        # * County Name
        # * Date
        # * The number of positive/negative tests
        # * The number of test kits the agent will distribute
        pass