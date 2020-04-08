class ResultConsumer:
    def consume_result(self, county, results):
        raise NotImplementedError("Subclass must implement abstract method")