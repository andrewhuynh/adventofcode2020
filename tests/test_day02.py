import unittest

from src.day02 import sled_password_checker, toboggan_password_checker


class TestPasswordPolicyChecker(unittest.TestCase):
    def test_sled_password_checker(self):
        self.assertEqual(2, sled_password_checker("day02_sample"))

    def test_toboggan_password_checker(self):
        self.assertEqual(1, toboggan_password_checker("day02_sample"))


if __name__ == '__main__':
    unittest.main()
