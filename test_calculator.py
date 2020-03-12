"""
Unit tests for the calculator library and app
"""
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(4, Calculator().add(2, 2))

    def test_subtraction(self):
        self.assertEqual(2, Calculator().subtract(4, 2))
    
    def test_multiplication(self):
        self.assertEqual(8, Calculator().multiplication(4, 2))
