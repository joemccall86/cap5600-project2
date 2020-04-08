from result_consumer import ResultConsumer


class PrintResultConsumer(ResultConsumer):
    def consume_result(self, county, results):
        """
        Simply print the results to STDOUT
        :param county: the county
        :param results: the results
        :return:
        """
        print(f"results for county {county.name}: {results}")