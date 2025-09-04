import unittest
from unittest.mock import patch
from io import StringIO
import sys

from main import main
from src.write_number import write_number
from src.const import INITIAL_AMOUNT
from tests.const import MENU, MESSAGES

class TestMainInteractive(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '4'])
    def test_view_balance_and_exit(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn(MENU["title"], output)
        self.assertIn(MESSAGES["current_balance"].format(write_number(INITIAL_AMOUNT)), output)
        self.assertIn(MENU["goodbye"], output)


    @patch('builtins.input', side_effect=['0', '5', 'a', '4'])
    def test_invalid_entry(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        for i in range(4):
            self.assertIn(MENU["invalid_choice"], output)
        self.assertIn(MENU["goodbye"], output)

    @patch('builtins.input', side_effect=['2', '500', '4'])
    def test_add_credit(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn(MESSAGES["amount_credited"].format(write_number(1500)), output)
        self.assertIn(MENU["goodbye"], output)


    @patch('builtins.input', side_effect=['3', '500', '4'])
    def test_debit_credit(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn(MESSAGES["amount_debited"].format(write_number(500)), output)
        self.assertIn(MENU["goodbye"], output)


    @patch('builtins.input', side_effect=['2', '750.23', '3', '500.89', '1', '3', '1250', '1', '4'])
    def test_successive_action(self, mock_input):
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn(MESSAGES["amount_credited"].format(write_number(1750.23)), output)
        self.assertIn(MESSAGES["amount_debited"].format(write_number(1249.34)), output)
        self.assertIn(MESSAGES["current_balance"].format(write_number(1249.34)), output)
        self.assertIn(MESSAGES["insufficient_funds"], output)
        self.assertIn(MESSAGES["current_balance"].format(write_number(1249.34)), output)
        self.assertIn(MENU["goodbye"], output)


if __name__ == "__main__":
    unittest.main()