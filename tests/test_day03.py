import unittest

from src.day03 import tree_encounters, multiply_tree_encounters


class TestTreeEncounters(unittest.TestCase):
    def test_tree_encounters_sample(self):
        self.assertEqual(7, tree_encounters("samples/day03_sample", 3, 1))

    def test_tree_encounters_input(self):
        self.assertEqual(167, tree_encounters("samples/day03_input", 3, 1))

    def test_multiply_tree_encounters_sample(self):
        self.assertEqual(336, multiply_tree_encounters("samples/day03_sample"))

    def test_multiply_tree_encounters_sample(self):
        self.assertEqual(736527114, multiply_tree_encounters("samples/day03_input"))


if __name__ == '__main__':
    unittest.main()
