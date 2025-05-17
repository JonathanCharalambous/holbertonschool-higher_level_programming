import unittest
from io import StringIO
from unittest.mock import patch
from text_indentation import text_indentation

class TestTextIndentation(unittest.TestCase):

    def test_basic_punctuation(self):
        text = "Hello. How are you? I'm fine: thanks."
        expected_output = (
            "Hello.\n\n"
            " How are you?\n\n"
            " I'm fine:\n\n"
            " thanks.\n\n"
        )
        with patch('sys.stdout', new=StringIO()) as mock_out:
            text_indentation(text)
            self.assertEqual(mock_out.getvalue(), expected_output)

    def test_text_without_punctuation(self):
        text = "This is just a simple string"
        expected_output = "This is just a simple string"
        with patch('sys.stdout', new=StringIO()) as mock_out:
            text_indentation(text)
            self.assertEqual(mock_out.getvalue(), expected_output)

    def test_empty_string(self):
        with patch('sys.stdout', new=StringIO()) as mock_out:
            text_indentation("")
            self.assertEqual(mock_out.getvalue(), "")

    def test_non_string_input(self):
        with self.assertRaises(TypeError) as cm:
            text_indentation(12345)
        self.assertEqual(str(cm.exception), "text must be a string")


if __name__ == '__main__':
    unittest.main()
