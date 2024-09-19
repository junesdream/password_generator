import unittest
from unittest.mock import patch
from io import StringIO

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import create_password

class TestCreatePassword(unittest.TestCase):

    @patch('builtins.input', side_effect=['12', 'y', 'y', 'y', 'y'])
    def test_password_length_and_composition(self, mock_input):
        password = create_password()

        # Check the length of the password
        self.assertEqual(len(password), 12)

        # heck that the password contains all types of characters
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?' for c in password))

    @patch('builtins.input', side_effect=['5', '8', 'n', 'n', 'n', 'n'])
    def test_minimum_length_and_default_charset(self, mock_input):
        password = create_password()

        # Check the minimum length of the password
        self.assertEqual(len(password), 8)

        # Check whether the password contains only lower case letters
        self.assertTrue(all(c.islower() for c in password))

    @patch('builtins.input', side_effect=['10', 'y', 'n', 'n', 'n'])
    def test_specific_charset(self, mock_input):
        password = create_password()

        # Check the length of the password
        self.assertEqual(len(password), 10)

        # Check whether the password contains only lower case letters
        self.assertTrue(all(c.islower() for c in password))

    @patch('builtins.input', side_effect=['abc', '8', 'y', 'y', 'y', 'y'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input_handling(self, mock_stdout, mock_input):
        password = create_password()

        # Check whether the error message has been issued
        self.assertIn("Please enter a valid number.", mock_stdout.getvalue())

        # Check the length of the password
        self.assertEqual(len(password), 8)


if __name__ == '__main__':
    unittest.main()