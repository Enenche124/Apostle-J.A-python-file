import unittest
import multiplyfunction
class TestMultiplicationFunction(unittest.TestCase):
    def test_that_multiplication_function_exist(self):
        multiplyfunction.get_result(3, 5)
    def test_that_multiplication_function_return_correct_value(self):
        actual = multiplyfunction.get_result(3, 5)
        results = 15
        self.assertEqual(actual, results)
    def test_that_multiplication_function_return_invalid_for_invalid_input(self):
        actual = multiplyfunction.get_result('a', 'a')
        results = "invalid input"
        self.assertEqual(actual, results)
    def test_that_multiplication_function_return_correct_value_for_decimal_value(self):
        actual = multiplyfunction.get_result(4.53, 3.25)
        results = 14.7225
        self.assertEqual(actual, results)