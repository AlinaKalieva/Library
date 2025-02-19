import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculator(-1,2)
        self.assertEqual(calculation.do_sum(), 1, 'The sum is wrong')

    def test_diff(self):
        calculation = Calculator(8, 2)
        self.assertEqual(calculation.do_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        calculation = Calculator(8, 2)
        self.assertEqual(calculation.do_product(), 16, 'The multiplication is wrong.')

    def test_quotient(self):
        calculation = Calculator(8, 2)
        self.assertEqual(calculation.do_division(), 4, 'The division is wrong.')

if __name__ == '__main__':
    unittest.main()