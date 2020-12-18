from unittest import TestCase

from src.day07 import get_color_count, get_number_of_bags_required, color_sum


class TestGetColorCount(TestCase):
    def test_get_color_count(self):
        self.assertEqual(4, get_color_count("samples/day07_sample_1"))
        self.assertEqual(179, get_color_count("samples/day07_input"))


class TestGetNumberOfBagsRequired(TestCase):
    def test_get_number_of_bags_required(self):
        self.assertEqual(32, get_number_of_bags_required("samples/day07_sample_1"))
        self.assertEqual(126, get_number_of_bags_required("samples/day07_sample_2"))
        self.assertEqual(2, get_number_of_bags_required("samples/day07_sample_3"))
        self.assertEqual(6, get_number_of_bags_required("samples/day07_sample_4"))
        self.assertEqual(4, get_number_of_bags_required("samples/day07_sample_5"))
        self.assertEqual(32, get_number_of_bags_required("samples/day07_sample_6"))
        self.assertEqual(18925, get_number_of_bags_required("samples/day07_input"))
