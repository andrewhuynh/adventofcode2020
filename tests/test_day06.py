from unittest import TestCase

from src.day06 import groups_sum, count_unanimous_yes


class TestGroupsSum(TestCase):
    def test_groups_sum(self):
        self.assertEqual(11, groups_sum("samples/day06_sample"))
        self.assertEqual(7283, groups_sum("samples/day06_input"))


class TestCountUnanimousYes(TestCase):
    def test_count_unanimous_yes(self):
        self.assertEqual(6, count_unanimous_yes("samples/day06_sample"))
        self.assertEqual(6, count_unanimous_yes("samples/day06_input"))
