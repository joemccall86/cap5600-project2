"""
/**
 * Implementation of a test kit evaluator that returns positive at a purely random rate
 *
 * @author Joe McCall; Chris Zahuranec
 * @date 4/24/2020
 * @info Course CAP5600
 */
"""
import random

from test_kit_evaluator import TestKitEvaluator


class RandomTestKitEvaluator(TestKitEvaluator):

    def evaluate_test(self, county, current_date):
        """
        Evaluate a test based on a random probability
        :return: True if the test is positive, False if negative
        """
        coin_flip = random.randint(0, 1)
        positive = coin_flip == 1
        return positive

    def update_county_data(self, county, current_date):
        """
        Pass-through since the random test kit evaluator does not keep internal data
        :param county:
        :param current_date:
        :return:
        """
        return
