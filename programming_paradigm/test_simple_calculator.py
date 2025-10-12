import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    # --- Required exact names ---
    def test_addition(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-5, 2), -3)
        self.assertAlmostEqual(self.calc.add(2.5, 0.5), 3.0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-4, 3), -12)
        self.assertEqual(self.calc.multiply(4, 0), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 1.2), 3.0)

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        # Edge case: division by zero returns None per implementation
        self.assertIsNone(self.calc.divide(10, 0))

    # --- Optional: type behavior (Python raises TypeError with invalid types) ---
    def test_type_errors(self):
        with self.assertRaises(TypeError):
            self.calc.add("2", 3)
        with self.assertRaises(TypeError):
            self.calc.subtract(5, "1")
        with self.assertRaises(TypeError):
            self.calc.multiply("a", 3.5)  # avoids valid string repetition "* 3"
        with self.assertRaises(TypeError):
            self.calc.divide("10", 2)

if __name__ == "__main__":
    unittest.main()
