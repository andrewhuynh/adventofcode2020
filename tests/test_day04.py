import unittest

from src.day04 import papers_please, stricter_papers_please


class TestReportRepair(unittest.TestCase):
    def test_papers_please_sample(self):
        self.assertEqual(2, papers_please("samples/day04_sample"))

    def test_papers_please_input(self):
        self.assertEqual(206, papers_please("samples/day04_input"))

    def test_stricter_papers_please_sample(self):
        self.assertEqual(4, stricter_papers_please("samples/day04_02_sample"))

    def test_stricter_papers_please_input(self):
        self.assertEqual(123, stricter_papers_please("samples/day04_input"))


if __name__ == '__main__':
    unittest.main()