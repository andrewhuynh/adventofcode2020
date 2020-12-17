import unittest

from src.day12 import manhattan_distance, manhattan_waypoint


class TestManhattanDistance(unittest.TestCase):
    def test_manhattan_distance_sample(self):
        self.assertEqual(25, manhattan_distance("day12_sample"))

    def test_manhattan_distance_input(self):
        self.assertEqual(582, manhattan_distance("day12_input"))

    def test_manhattan_waypoint_sample(self):
        self.assertEqual(286, manhattan_waypoint("day12_sample"))

    def test_manhattan_waypoint_input(self):
        self.assertEqual(52069, manhattan_waypoint("day12_input"))


if __name__ == '__main__':
    unittest.main()
