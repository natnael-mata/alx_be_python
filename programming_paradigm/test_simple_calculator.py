import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(1, 0), 1)
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply(self):
        """Test the multiplcation method"""
        self.assertEqual(self.calc.multiply(100, 0), 0)
        self.assertEqual(self.calc.multiply(10, 10), 100)
    def test_divide(self):
        """Test the dividion method"""
        self.assertEqual(self.calc.multiply(100, 10), 10)
        self.assertEqual(self.calc.multiply(1, 2), 0.5)
                # ⚠️ Zero division case
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)
    if __name__ == '__main__':
        unittest.main()