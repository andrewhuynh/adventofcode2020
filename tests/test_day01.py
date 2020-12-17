import unittest

from src.day01 import fun, report_repair_two, report_repair_three


class TestFun(unittest.TestCase):
    def test_fun(self):
        self.assertEqual(fun(3), 4)


class TestReportRepair(unittest.TestCase):
    def test_report_repair_two(self):
        self.assertEqual(514579, report_repair_two("tests/day01_sample"))

    def test_report_repair_three(self):
        self.assertEqual(241861950, report_repair_three("tests/day01_sample"))


if __name__ == '__main__':
    unittest.main()