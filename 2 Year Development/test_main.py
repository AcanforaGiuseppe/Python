# import imported_file

# print("CANE")

# # Main del programma
# if __name__ == '__main__':
#     print("I am the main of test_main")

from main import my_func
import unittest


class TestMyFunc(unittest.TestCase):

    def test_my_func_divides_positive_numbers(self):
        self.assertEqual(my_func(3, 3), 1)

    def test_my_func_divides_negative_numbers(self):
        self.assertEqual(my_func(-5, -1), -5)

    def test_my_func_raises_error_for_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            my_func(1, 0)

# Try the test with the code:
# python -m unittest
