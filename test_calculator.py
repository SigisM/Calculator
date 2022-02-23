import unittest
from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def test_division_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.division, 5, 0)

    def test_complex_numbers(self):
        self.assertRaises(ValueError, self.calc.nth_root, -5, 2)

    def test_addition_two_arguments(self):
        self.assertEqual(self.calc.addition(10, 20), 30)
        self.assertEqual(self.calc.addition(1.5, 2.3), 3.8)
        self.assertEqual(self.calc.addition(-5, -2), -7)

    def test_addition_one_argument(self):
        self.calc.memory = 2
        self.assertEqual(self.calc.addition(30), 32)

    def test_subtraction_two_arguments(self):
        self.assertEqual(self.calc.subtraction(33, 3), 30)
        self.assertEqual(self.calc.subtraction(3, 33), -30)

    def test_subtraction_one_argument(self):
        self.calc.memory = 100
        self.assertEqual(self.calc.subtraction(90), 10)

    def test_multiplication_two_arguments(self):
        self.assertEqual(self.calc.multiplication(9, 2), 18)
        self.assertEqual(self.calc.multiplication(9.5, 2), 19.0)

    def test_multiplication_one_argument(self):
        self.calc.memory = 100
        self.assertEqual(self.calc.multiplication(0.5), 50.0)

    def test_division_two_arguments(self):
        self.assertEqual(self.calc.division(9, 2), 4.5)
        self.assertEqual(self.calc.division(0, 2), 0)

    def test_division_one_argument(self):
        self.calc.memory = 100
        self.assertEqual(self.calc.division(0.5), 200.0)

    def test_nroot_two_arguments(self):
        self.assertEqual(self.calc.nth_root(125, 3), 5)
        self.assertEqual(self.calc.nth_root(256, 8), 2)
        self.assertEqual(self.calc.nth_root(0, 8), 0)

    def test_nroot_one_argument(self):
        self.calc.memory = 512
        self.assertEqual(self.calc.nth_root(9), 2)
        self.calc.memory = 0
        self.assertEqual(self.calc.nth_root(9), 0)

    def test_input_validity(self):
        self.assertRaises(TypeError, self.calc._input_validation, '@', 2)
        self.assertRaises(TypeError, self.calc._input_validation, 2, '@')
        self.assertRaises(TypeError, self.calc._input_validation, '.', ',')


if __name__ == '__main__':
    unittest.main()
