import unittest
from math_help import add, subtract, divide, sqrt

class TestAddFunction(unittest.TestCase):

    def test_twoPositiveNumbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_twoNegativeNumbers(self):
        self.assertEqual(add(-1, -3), -4)

    def test_oneNegatvieOnePositiveNumber(self):
        self.assertEqual(add(-1, 1), 0)

    def test_wrongParameter(self):
        self.assertEqual(add("1", 2), "ensure parameters are integers")

class TestSubtractFunction(unittest.TestCase):

    def test_twoPositiveNumbers(self):
        self.assertEqual(subtract(3, 2), 1)
    
    def test_twoNegativeNumbers(self):
        self.assertEqual(subtract(-3, -4), 1)

    def test_oneNegativeOnePositiveNumber(self):
        self.assertEqual(subtract(-5, 5), -10)

    def test_wrongParameter(self):
        self.assertEqual(subtract("-5", -10), "ensure parameters are integers")

class TestDivideFunction(unittest.TestCase):

    def test_twoPositiveNumbers(self):
        self.assertEqual(divide(10, 5), 2)

    def test_twoNegativeNumbers(self):
        self.assertEqual(divide(-15, -3), 5)
    
    def test_oneNegativeOnePositive(self):
        self.assertEqual(divide(-20, 2), -10)

    def test_wrongParameter(self):
        self.assertEqual(divide("10", 2), "ensure parameters are integers")


class TestSqrtFunction(unittest.TestCase):

    def test_positiveNumber(self):
        self.assertEqual(sqrt(9), 3)
    
    def test_negativeNumber(self):
        self.assertEqual(sqrt(-9), "num must be > 0")

    def test_wrongParameter(self):
        self.assertEqual(sqrt("144"), "ensure parameters are integers")

if __name__ == "__main__":
    unittest.main()