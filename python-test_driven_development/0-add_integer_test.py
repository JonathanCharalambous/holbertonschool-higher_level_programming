#!/usr/bin/python3
from add_integer import add_integer
import unittest


class TestAddInteger(unittest.TestCase):

    def test_add_two_integers(self):
        self.assertEqual(add_integer(2, 3), 5)

    def test_add_integer_and_default(self):
        self.assertEqual(add_integer(2), 100)

    def test_add_floats(self):
        self.assertEqual(add_integer(3.7, 2.3), 5)

    def test_first_argument_type_error(self):
        with self.assertRaises(TypeError):
            add_integer("a", 2)

    def test_second_argument_type_error(self):
        with self.assertRaises(TypeError):
            add_integer(2, "b")

if __name__ == '__main__':
    unittest.main()