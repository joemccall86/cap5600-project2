class ResultConsumer:
    def consume_result(self, county, date, results):
        raise NotImplementedError("Subclass must implement abstract method")