import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.calculation = Calculator(8,2)

    def test_sum(self):
        self.assertEqual(self.calculation.do_sum(), 10, 'The sum is wrong')

    def test_diff(self):
        self.assertEqual(self.calculation.do_difference(), 2, 'The difference is wrong.')

    def test_product(self):
        self.assertEqual(self.calculation.do_product(), 16, 'The multiplication is wrong.')

    def test_quotient(self):
        self.assertEqual(self.calculation.do_division(), 4, 'The division is wrong.')

if __name__ == '__main__':
    unittest.main()