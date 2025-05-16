#!/usr/bin/python3
import unittest
from matrix_divided import matrix_divided

class TestMatrixDivided(unittest.TestCase):

    def test_valid_matrix_and_div(self):
        self.assertEqual(
            matrix_divided([[4, 8], [12, 16]], 4),
            [[1.0, 2.0], [3.0, 4.0]]
        )

    def test_floats_and_division(self):
        self.assertEqual(
            matrix_divided([[3.0, 6.0], [9.0, 12.0]], 3),
            [[1.0, 2.0], [3.0, 4.0]]
        )

    def test_division_result_rounded(self):
        self.assertEqual(
            matrix_divided([[1, 2], [3, 4]], 3),
            [[0.33, 0.67], [1.0, 1.33]]
        )

    def test_invalid_matrix_not_list(self):
        with self.assertRaises(TypeError):
            matrix_divided("not a matrix", 2)

    def test_invalid_row_not_list(self):
        with self.assertRaises(TypeError):
            matrix_divided([[1, 2], "bad row"], 2)

    def test_invalid_element_not_number(self):
        with self.assertRaises(TypeError):
            matrix_divided([[1, 2], [3, "four"]], 2)

    def test_unequal_row_sizes(self):
        with self.assertRaises(TypeError):
            matrix_divided([[1, 2], [3, 4, 5]], 2)

    def test_div_not_number(self):
        with self.assertRaises(TypeError):
            matrix_divided([[1, 2], [3, 4]], "a")

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):
            matrix_divided([[1, 2], [3, 4]], 0)

if __name__ == '__main__':
    unittest.main()
