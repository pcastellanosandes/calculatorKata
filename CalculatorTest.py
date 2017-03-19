from unittest import TestCase

from Calculator import Calculator

__autor__ = 'Paula Castellanos'


class CalculatorTest(TestCase):
    def test_add(self):
        self.assertEqual(Calculator().add(""), 0, "empty string")
