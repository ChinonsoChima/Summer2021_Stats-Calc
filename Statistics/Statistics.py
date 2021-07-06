from Calculator.Calculator import Calculator
from Statistics.StatOperations.StatsOps import StatsOps


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = StatsOps.mean(data)
        return self.result

    def median(self, data):
        self.result = StatsOps.median(data)
        return self.result

    def mode(self, data):
        self.result = StatsOps.mode(data)
        return self.result

    def variance(self, data):
        self.result = StatsOps.variance(data)
        return self.result

    def std_deviation(self, data):
        self.result = StatsOps.std_deviation(data)
        return self.result

    def z_score(self, data):
        self.result = StatsOps.z_score(data)
        return self.result