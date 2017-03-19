from unittest import TestCase
import  Calculator


class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(""), 0, "empty string")
