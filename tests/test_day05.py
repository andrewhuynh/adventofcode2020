import unittest
from unittest import TestCase

from src.day05 import get_row, get_column, get_seat_id, get_highest_seat_id, get_missing_seat_id


class TestGetRow(TestCase):
    def test_get_row(self):
        self.assertEqual(44, get_row("FBFBBFFRLR"))
        self.assertEqual(127, get_row("BBBBBBBRLR"))
        self.assertEqual(70, get_row("BFFFBBFRRR"))
        self.assertEqual(14, get_row("FFFBBBFRRR"))
        self.assertEqual(102, get_row("BBFFBBFRLL"))


class TestGetColumn(TestCase):
    def test_get_column(self):
        self.assertEqual(5, get_column("FBFBBFFRLR"))
        self.assertEqual(7, get_column("BFFFBBFRRR"))
        self.assertEqual(7, get_column("FFFBBBFRRR"))
        self.assertEqual(4, get_column("BBFFBBFRLL"))


class TestGetSeatId(TestCase):
    def test_get_seat_id(self):
        self.assertEqual(357, get_seat_id("FBFBBFFRLR"))
        self.assertEqual(567, get_seat_id("BFFFBBFRRR"))
        self.assertEqual(119, get_seat_id("FFFBBBFRRR"))
        self.assertEqual(820, get_seat_id("BBFFBBFRLL"))


class TestGetHighestSeatId(TestCase):
    def test_get_highest_seat_id(self):
        self.assertEqual(820, get_highest_seat_id("samples/day05_sample"))
        self.assertEqual(970, get_highest_seat_id("samples/day05_input"))


class TestGetMissingSeatId(TestCase):
    def test_get_missing_seat_id(self):
        self.assertEqual(587, get_missing_seat_id("samples/day05_input"))


if __name__ == '__main__':
    unittest.main()