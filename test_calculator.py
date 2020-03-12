"""
Unit tests for the calculator library
"""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(4, Calculator().add(2, 2))

    def test_subtraction(self):
        self.assertEqual(2, Calculator().subtract(4, 2))
