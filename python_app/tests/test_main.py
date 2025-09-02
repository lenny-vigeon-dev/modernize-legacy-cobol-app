import unittest
from unittest.mock import patch
from io import StringIO
import sys

from main import main

class TestMainInteractive(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '4'])
    def test_view_balance_and_exit(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Account Management System", output)
        self.assertIn("Current balance: 1000.00", output)
        self.assertIn("Exiting the program. Goodbye!", output)

if __name__ == "__main__":
    unittest.main()