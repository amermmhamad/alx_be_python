import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition ---
    def test_addition_basic(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_floats_and_large(self):
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)
        self.assertEqual(self.calc.add(10**6, 10**6), 2_000_000)

    def test_addition_commutative(self):
        a, b = 7, -3
        self.assertEqual(self.calc.add(a, b), self.calc.add(b, a))

    # --- Subtraction ---
    def test_subtraction_basic(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtraction_with_negatives(self):
        self.assertEqual(self.calc.subtract(-4, -6), 2)
        self.assertEqual(self.calc.subtract(-4, 6), -10)

    def test_subtraction_non_commutative(self):
        a, b = 9, 2
        self.assertNotEqual(self.calc.subtract(a, b), self.calc.subtract(b, a))

    # --- Multiplication ---
    def test_multiplication_basic(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-4, 3), -12)
        self.assertEqual(self.calc.multiply(4, 0), 0)

    def test_multiplication_floats_and_large(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 1.2), 3.0)
        self.assertEqual(self.calc.multiply(10**3, 10**3), 1_000_000)

    def test_multiplication_commutative(self):
        a, b = -7, 5
        self.assertEqual(self.calc.multiply(a, b), self.calc.multiply(b, a))

    # --- Division ---
    def test_division_basic(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_negative_and_float(self):
        self.assertAlmostEqual(self.calc.divide(-9, 2), -4.5)
        self.assertAlmostEqual(self.calc.divide(2.5, 0.5), 5.0)

    def test_division_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(10, 0))

    # --- Type and invalid input behavior (Python raises TypeError) ---
    def test_type_errors(self):
        with self.assertRaises(TypeError):
            self.calc.add("2", 3)
        with self.assertRaises(TypeError):
            self.calc.subtract(5, "1")
        with self.assertRaises(TypeError):
            self.calc.multiply("a", 3.5)  # "* 3" is valid string repetition; 3.5 raises TypeError
        with self.assertRaises(TypeError):
            self.calc.divide("10", 2)

if __name__ == "__main__":
    unittest.main()
