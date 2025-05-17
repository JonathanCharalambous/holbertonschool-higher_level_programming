#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch
from print_square import print_square

class TestPrintSquare(unittest.TestCase):

    def test_square_size_1(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            print_square(1)
            self.assertEqual(mock_out.getvalue(), "#\n")

    def test_square_size_3(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            print_square(3)
            self.assertEqual(mock_out.getvalue(), "###\n###\n###\n")

    def test_size_zero(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            print_square(0)
            self.assertEqual(mock_out.getvalue(), "")

    def test_size_negative(self):
        with self.assertRaises(ValueError) as cm:
            print_square(-2)
        self.assertEqual(str(cm.exception), "Size must be >= 0")

    def test_size_not_integer(self):
        with self.assertRaises(TypeError) as cm:
            print_square("4")
        self.assertEqual(str(cm.exception), "Size must be an integer")

    def test_size_float_positive(self):
        with self.assertRaises(TypeError) as cm:
            print_square(2.5)
        self.assertEqual(str(cm.exception), "Size must be an integer")

if __name__ == '__main__':
    unittest.main()
