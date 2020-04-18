from datetime import datetime


class TestKitEvaluator:

    def evaluate_test(self, county, current_date):
        raise NotImplementedError("Subclass must implement abstract method")

    def update_county_data(self, county, current_date):
        raise NotImplementedError("Subclass must implement abstract method")
