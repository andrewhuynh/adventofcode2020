from unittest import TestCase

from src.day18 import weird_arithmetic, handle_parentheses, solve_it, operation_order, add_parentheses_for_addition, \
    solve_it_part_two, add_parentheses_for_addition_complex, operation_order_part_two


class TestWeirdArithmetic(TestCase):
    def test_weird_arithmetic(self):
        self.assertEqual(6810, weird_arithmetic("54*126+6"))
        self.assertEqual(20, weird_arithmetic("2 + 3 * 4"))
        self.assertEqual(30, weird_arithmetic("4 + 6 + 20"))


class TestHandleParentheses(TestCase):
    def test_handle_parentheses(self):
        self.assertEqual("2*3+20", handle_parentheses("2 * 3 + (4 * 5)"))
        self.assertEqual("4+26", handle_parentheses("4 + ((2 * 3) + (4 * 5))"))


class TestSolveIt(TestCase):
    def test_solve_it(self):
        self.assertEqual(26, solve_it("2 * 3 + (4 * 5)"))
        self.assertEqual(437, solve_it("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
        self.assertEqual(12240, solve_it("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
        self.assertEqual(13632, solve_it("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))
        self.assertEqual(15, solve_it("(((2+3))+((4+6)))"))


class TestOperationOrder(TestCase):
    def test_operation_order(self):
        self.assertEqual(71, operation_order("samples/day18_sample"))
        self.assertEqual(26335, operation_order("samples/day18_sample_2"))
        self.assertEqual(45283905029161, operation_order("samples/day18_input"))


class TestWeirderArithmetic(TestCase):
    def test_weirder_arithmetic(self):
        self.assertEqual("(1+2)*(3+4)*(5+6)", add_parentheses_for_addition("1 + 2 * 3 + 4 * 5 + 6"))
        self.assertEqual("(10+20)*(30+40)*(50+60)", add_parentheses_for_addition("10 + 20 * 30 + 40 * 50 + 60"))


class TestAddParenthesesForAdditionComplex(TestCase):
    def test_add_parentheses_for_addition_complex(self):
        self.assertEqual("3*((2*3)+(4*5))", add_parentheses_for_addition_complex("3*(2*3)+(4*5)"))
        self.assertEqual("(((2+3))+((4+6)))", add_parentheses_for_addition_complex("(2+3)+(4+6)"))


class TestSolveItPartTwo(TestCase):
    def test_solve_it_part_two(self):
        self.assertEqual(231, solve_it_part_two("1 + 2 * 3 + 4 * 5 + 6"))
        self.assertEqual(231000, solve_it_part_two("10 + 20 * 30 + 40 * 50 + 60"))
        self.assertEqual(51, solve_it_part_two("1 + (2 * 3) + (4 * (5 + 6))"))
        self.assertEqual(46, solve_it_part_two("2 * 3 + (4 * 5)"))
        self.assertEqual(1445, solve_it_part_two("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
        self.assertEqual(669060, solve_it_part_two("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
        self.assertEqual(23340, solve_it_part_two("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))


class TestOperationOrderPartTwo(TestCase):
    def test_operation_order_part_two(self):
        self.assertEqual(51, operation_order_part_two("samples/day18_sample_3"))
        self.assertEqual(693891, operation_order_part_two("samples/day18_sample_2"))
        self.assertEqual(216975281211165, operation_order_part_two("samples/day18_input"))
