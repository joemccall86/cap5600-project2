"""
/**
 * Implementation of a result consumer that simply prints the results
 *
 * @author Joe McCall; Chris Zahuranec
 * @date 4/24/2020
 * @info Course CAP5600
 */
"""
from result_consumer import ResultConsumer


class PrintResultConsumer(ResultConsumer):
    def consume_result(self, county, date, results):
        """
        Simply print the results to STDOUT
        :param county: the county
        :param date: the date
        :param results: the results
        :return:
        """
        print(f"results for county {county.name}: {results} out of {county.num_actual_positive_cases}")