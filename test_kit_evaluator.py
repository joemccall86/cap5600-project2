from datetime import datetime


class TestKitEvaluator:

    current_date: datetime

    def __init__(self, current_date):
        self.current_date = current_date

    def evaluate_test(self, county):
        raise NotImplementedError("Subclass must implement abstract method")
