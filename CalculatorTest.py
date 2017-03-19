from unittest import TestCase

from Calculator import Calculator

__autor__ = 'Paula Castellanos'


class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(""), 0, "empty string")

    def test_addOneNumber(self):
        self.assertEqual(Calculator().add("1"), 1, "One number")