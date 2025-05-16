#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from say_my_name import say_my_name

class TestSayMyName(unittest.TestCase):

    def test_valid_full_name(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            say_my_name("John", "Doe")
            self.assertEqual(mock_out.getvalue().strip(), "My name is John Doe")

    def test_valid_first_name_only(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            say_my_name("Alice")
            self.assertEqual(mock_out.getvalue(), "My name is Alice \n")

    def test_first_name_not_string(self):
        with self.assertRaises(TypeError) as cm:
            say_my_name(123, "Smith")
        self.assertEqual(str(cm.exception), "first_name must be a string")

    def test_last_name_not_string(self):
        with self.assertRaises(TypeError) as cm:
            say_my_name("Jane", 456)
        self.assertEqual(str(cm.exception), "last_name must be a string")

    
    def test_both_names_empty_strings(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            say_my_name("", "")
        self.assertEqual(mock_out.getvalue(), "My name is  \n")

if __name__ == '__main__':
    unittest.main()