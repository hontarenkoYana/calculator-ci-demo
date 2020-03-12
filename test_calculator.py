"""
Unit tests for the calculator library and app
"""
import app
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_addition(self):
        self.assertEqual(4, Calculator().add(2, 2))

    def test_subtraction(self):
        self.assertEqual(2, Calculator().subtract(4, 2))

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')
