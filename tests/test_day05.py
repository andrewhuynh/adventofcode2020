import unittest

from src.day05 import highest_seat, highester_seat


class TestHighestSeat(unittest.TestCase):
    def test_highest_seat_sample(self):
        self.assertEqual(820, highest_seat("day05_sample"))

    def test_highest_seat_input(self):
        self.assertEqual(0, highest_seat("day05_input"))

    def test_stricter_papers_please_sample(self):
       self.assertEqual(0, highester_seat("day05_sample"))

    def test_stricter_papers_please_input(self):
        self.assertEqual(0, highester_seat("day05_input"))


if __name__ == '__main__':
    unittest.main()