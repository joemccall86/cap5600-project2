"""
/**
 * static class to encapsulate a scoring strategy
 *
 * @author Joe McCall; Chris Zahuranec
 * @date 4/24/2020
 * @info Course CAP5600
 */
"""


class ScoringStrategy:
    @classmethod
    def compute_score(cls, county):
        """
        Compute the score for a county
        :param county: the county object
        :return: the score
        """
        return (10 * county.num_measured_positive_cases) + county.num_measured_negative_cases
        # return abs(county.num_actual_positive_cases - county.num_measured_positive_cases)
