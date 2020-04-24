"""
/**
 * An abstract result consumer
 *
 * @author Joe McCall; Chris Zahuranec
 * @date 4/24/2020
 * @info Course CAP5600
 */
"""
class ResultConsumer:
    def consume_result(self, county, date, results):
        """
        Consume the results from a county (to be implemented)
        :param county: the county
        :param date: the date of the results
        :param results: the count of positive results
        :return:
        """
        raise NotImplementedError("Subclass must implement abstract method")