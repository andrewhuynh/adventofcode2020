from unittest import TestCase

from src.day08 import get_acc_before_loop, get_acc_and_check, get_acc_for_finite_program


class TestGetAccBeforeLoop(TestCase):
    def test_get_acc_before_loop(self):
        self.assertEqual(5, get_acc_before_loop("samples/day08_sample"))
        self.assertEqual(1446, get_acc_before_loop("samples/day08_input"))


# class TestGetAccAfterFix(TestCase):
#     def test_get_acc_after_fix(self):
#         # self.assertEqual(0, get_acc_after_fix("samples/day08_sample"))
#         self.assertEqual(0, get_acc_after_fix("samples/day08_input"))

class TestGetAccAndCheck(TestCase):
    def test_get_acc_and_check(self):
        with open("samples/day08_sample", "r") as f_01:
            boot_code_01 = [instruction.strip().split(" ") for instruction in f_01.readlines()]
            self.assertEqual([5, False], get_acc_and_check(boot_code_01))
        with open("samples/day08_input", "r") as f_02:
            boot_code_02 = [instruction.strip().split(" ") for instruction in f_02.readlines()]
            self.assertEqual([1446, False], get_acc_and_check(boot_code_02))
        with open("samples/day08_sample_2", "r") as f_03:
            boot_code_03 = [instruction.strip().split(" ") for instruction in f_03.readlines()]
            self.assertEqual([8, True], get_acc_and_check(boot_code_03))


class TestGetAccForFiniteProgram(TestCase):
    def test_get_acc_for_finite_program(self):
        self.assertEqual(8, get_acc_for_finite_program("samples/day08_sample_2"))
        self.assertEqual(8, get_acc_for_finite_program("samples/day08_sample"))
        self.assertEqual(1403, get_acc_for_finite_program("samples/day08_input"))
