import unittest
from src.data_program import DataProgram
from src.operations import Operations
from src.write_number import write_number
from src.const import INITIAL_AMOUNT
from tests.const import MESSAGES

class TestOperations(unittest.TestCase):
    dp: DataProgram
    ops: Operations

    def setUp(self):
        self.dp = DataProgram()
        self.ops = Operations(self.dp)

    def test_total(self):
        # Capture print output
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        self.ops.total()
        sys.stdout = sys.__stdout__
        self.assertIn(MESSAGES["current_balance"].format(write_number(INITIAL_AMOUNT)), captured.getvalue())

    def test_credit(self):
        # Simulate input and capture print
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        sys.stdin = io.StringIO("200.50\n")
        self.ops.credit()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertIn(MESSAGES["amount_credited"].format(write_number(1200.5)), captured.getvalue())

    def test_credit_int(self):
        # Simulate input and capture print
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        sys.stdin = io.StringIO("144\n")
        self.ops.credit()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertIn(MESSAGES["amount_credited"].format(write_number(1144)), captured.getvalue())

    def test_credit_dec(self):
        # Simulate input and capture print
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        sys.stdin = io.StringIO("0.75\n")
        self.ops.credit()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertIn(MESSAGES["amount_credited"].format(write_number(1000.75)), captured.getvalue())

    def test_credit_0(self):
        # Simulate input and capture print
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        sys.stdin = io.StringIO("0\n")
        self.ops.credit()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertIn(MESSAGES["amount_credited"].format(write_number(INITIAL_AMOUNT)), captured.getvalue())

    def test_debit_success(self):
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        sys.stdin = io.StringIO("500.00\n")
        self.ops.debit()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertIn(MESSAGES["amount_debited"].format(write_number(500)), captured.getvalue())

    def test_debit_insufficient(self):
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        sys.stdin = io.StringIO("2000.00\n")
        self.ops.debit()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertIn(MESSAGES["insufficient_funds"], captured.getvalue())

    def test_debit_0(self):
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        sys.stdin = io.StringIO("0\n")
        self.ops.debit()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertIn(MESSAGES["amount_debited"].format(write_number(INITIAL_AMOUNT)), captured.getvalue())

if __name__ == "__main__":
    unittest.main()
