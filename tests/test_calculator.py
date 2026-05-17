import unittest
from calculator import add, subtract, multiply, divide, power, modulo

class TestCalculator(unittest.TestCase):
    """Unit tests for all arithmetic operations in calculator.py."""

    def test_add(self) -> None:
        """Test addition of two numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)

    def test_subtract(self) -> None:
        """Test subtraction of two numbers."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-5, -5), 0)
        self.assertEqual(subtract(0, 7), -7)
        self.assertAlmostEqual(subtract(3.5, 1.2), 2.3)

    def test_multiply(self) -> None:
        """Test multiplication of two numbers."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)
        self.assertAlmostEqual(multiply(2.5, 0.4), 1.0)

    def test_divide(self) -> None:
        """Test division of two numbers (non‑zero divisor)."""
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 1/3)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self) -> None:
        """Test that division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_power(self) -> None:
        """Test exponentiation."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertAlmostEqual(power(4, 0.5), 2)
        self.assertAlmostEqual(power(10, -2), 0.01)

    def test_modulo(self) -> None:
        """Test modulus operation."""
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(7, -3), -2)
        self.assertEqual(modulo(0, 5), 0)
        self.assertAlmostEqual(modulo(3.5, 1.2), 1.1)

    def test_negative_numbers(self) -> None:
        """Test operations with negative numbers."""
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(subtract(-10, -5), -5)
        self.assertEqual(multiply(-4, 3), -12)
        self.assertEqual(divide(-9, 3), -3)

if __name__ == '__main__':
    unittest.main()