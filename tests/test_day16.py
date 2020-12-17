import unittest

from src.day16 import scanning_error_rate


class TestScanningErrorRate(unittest.TestCase):
    def test_error_rate_sample(self):
        self.assertEqual(71, scanning_error_rate("day16_sample"))

    # def test_error_rate_input(self):
    #     self.assertEqual(0, scanning_error_rate("day16_input"))

    # def test_manhattan_waypoint_sample(self):
    #     self.assertEqual(0, scanning_error_rate_2("day16_sample"))

    # def test_manhattan_waypoint_input(self):
    #     self.assertEqual(0, scanning_error_rate_2("day16_input"))


if __name__ == '__main__':
    unittest.main()
