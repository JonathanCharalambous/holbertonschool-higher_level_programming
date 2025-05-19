#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-3, -5, -2, -10]), -2)

    def test_mixed_positive_and_negative(self):
        self.assertEqual(max_integer([-1, 3, 5, -7]), 5)

    def test_all_same(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 0.5]), 3.3)

    def test_string_list(self):
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_string_input(self):
        self.assertEqual(max_integer("hello"), "o")

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
