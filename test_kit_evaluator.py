"""
/**
 * Abstract test kit evaluator
 *
 * @author Joe McCall; Chris Zahuranec
 * @date 4/24/2020
 * @info Course CAP5600
 */
"""


class TestKitEvaluator:

    def evaluate_test(self, county, current_date):
        """
        evaluate a single test for a county
        :param county: the county
        :param current_date: the current date
        :return: true if the test is positive, false otherwise
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def update_county_data(self, county, current_date):
        """
        Update internal data if needed
        :param county: the county object
        :param current_date: the current date
        :return:
        """
        raise NotImplementedError("Subclass must implement abstract method")
