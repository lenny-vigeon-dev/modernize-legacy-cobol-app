import unittest
from unittest.mock import patch
from io import StringIO
import sys

from main import main
from src.write_number import write_number

class TestMainInteractive(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '4'])
    def test_view_balance_and_exit(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Account Management System", output)
        self.assertIn(f"Current balance: {write_number(1000)}", output)
        self.assertIn("Exiting the program. Goodbye!", output)


    @patch('builtins.input', side_effect=['0', '5', 'a', '4'])
    def test_invalid_entry(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        for i in range(4):
            self.assertIn("Invalid choice, please select 1-4.", output)
        self.assertIn("Exiting the program. Goodbye!", output)

    @patch('builtins.input', side_effect=['2', '500', '4'])
    def test_add_credit(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn(f"Amount credited. New balance: {write_number(1500)}", output)
        self.assertIn("Exiting the program. Goodbye!", output)


    @patch('builtins.input', side_effect=['3', '500', '4'])
    def test_debit_credit(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn(f"Amount debited. New balance: {write_number(500)}", output)
        self.assertIn("Exiting the program. Goodbye!", output)


    @patch('builtins.input', side_effect=['2', '750.23', '3', '500.89', '1', '3', '1250', '1', '4'])
    def test_successive_action(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn(f"Amount credited. New balance: {write_number(1750.23)}", output)
        self.assertIn(f"Amount debited. New balance: {write_number(1249.34)}", output)
        self.assertIn(f"Current balance: {write_number(1249.34)}", output)
        self.assertIn(f"Insufficient funds for this debit.", output)
        self.assertIn(f"Current balance: {write_number(1249.34)}", output)
        self.assertIn("Exiting the program. Goodbye!", output)


if __name__ == "__main__":
    unittest.main()