class ScoringStrategy:
    @classmethod
    def compute_score(cls, county):
        return (10 * county.num_measured_positive_cases) + county.num_measured_negative_cases
        # return abs(county.num_actual_positive_cases - county.num_measured_positive_cases)
