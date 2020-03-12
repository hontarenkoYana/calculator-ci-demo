"""
Unit tests for the calculator library and app
"""
import app
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_main(self):
        rv = self.app.get('/')
        self.assertEqual('200 OK', rv.status)

    def test_addition(self):
        params = {"first_term": 2, "second_term": 3}
        rv = self.app.post('/addition', data=params)
        self.assertEqual(rv.status, '200 OK')
        self.assertIn("5", rv.data.decode("utf-8"))

    def test_substraction(self):
        params = {"first_term": 4, "second_term": 2}
        rv = self.app.post('/substraction', data=params)
        self.assertEqual(rv.status, '200 OK')
        self.assertIn("2", rv.data.decode("utf-8"))

    def test_multiplication(self):
        params = {"first_term": 3, "second_term": 3}
        rv = self.app.post('/multiplication', data=params)
        self.assertEqual(rv.status, '200 OK')
        self.assertIn("9", rv.data.decode("utf-8"))
