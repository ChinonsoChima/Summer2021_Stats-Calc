import unittest
import numpy as np
from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_results_property_calculator(self):
        self.assertEqual(self.statistics.result, 0)

    def test_mean_method_statistics(self):
        self.assertEqual(self.statistics.mean([1, 2, 3]), 2)
        self.assertEqual(self.statistics.result, 2)

    def test_median_method_statistics(self):
        # array odd length
        self.assertEqual(self.statistics.median([1, 3, 2]), 2)
        self.assertEqual(self.statistics.result, 2)

        # array with even length
        self.assertEqual(self.statistics.median([3, 4, 1, 2]), 2.5)
        self.assertEqual(self.statistics.result, 2.5)

    def test_mod_method_statistics(self):
        self.assertEqual(self.statistics.mode([1, 2, 2, 3, 3, 2]), 2)
        self.assertEqual(self.statistics.result, 2)

    def test_variance_method_statistics(self):
        self.assertEqual(self.statistics.variance([6, 3, 8, 5, 3]), 3.6)
        self.assertEqual(self.statistics.result, 3.6)

    def test_std_deviation_method_statistics(self):
        self.assertEqual(self.statistics.std_deviation([6, 3, 8, 5, 3]), 1.8973666)
        self.assertEqual(self.statistics.result, 1.8973666)

    def test_z_score_method_statistics(self):
        data_input = [0.7972, 0.0767, 0.4383, 0.7866, 0.8091, 0.1954, 0.6307, 0.6599, 0.1065, 0.0508]
        output = [1.1272, -1.247, -0.0554, 1.0923, 1.1665, -0.8558, 0.5786, 0.6748, -1.1488, -1.3323]

        self.assertEqual(self.statistics.z_score(data_input), output)
        self.assertEqual(self.statistics.result, output)

    def test_empty_data_list(self):
        self.assertEqual(self.statistics.mean([]), "Error: empty data list")
        self.assertEqual(self.statistics.result, "Error: empty data list")

        self.assertEqual(self.statistics.median([]), "Error: empty data list")
        self.assertEqual(self.statistics.result, "Error: empty data list")

        self.assertEqual(self.statistics.mode([]), "Error: empty data list")
        self.assertEqual(self.statistics.result, "Error: empty data list")

        self.assertEqual(self.statistics.variance([]), "Error: empty data list")
        self.assertEqual(self.statistics.result, "Error: empty data list")

        self.assertEqual(self.statistics.std_deviation([]), "Error: empty data list")
        self.assertEqual(self.statistics.result, "Error: empty data list")

        self.assertEqual(self.statistics.z_score([]), "Error: empty data list")
        self.assertEqual(self.statistics.result, "Error: empty data list")