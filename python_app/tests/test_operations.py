import unittest
from src.data_program import DataProgram
from src.operations import Operations

class TestOperations(unittest.TestCase):
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
        self.assertIn("Current balance: 1000.00", captured.getvalue())

    def test_credit(self):
        # Simulate input and capture print
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        sys.stdin = io.StringIO("200.50\n")
        self.ops.credit()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertIn("Amount credited. New balance: 1200.50", captured.getvalue())

    def test_debit_success(self):
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        sys.stdin = io.StringIO("500.00\n")
        self.ops.debit()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertIn("Amount debited. New balance: 500.00", captured.getvalue())

    def test_debit_insufficient(self):
        import io, sys
        captured = io.StringIO()
        sys.stdout = captured
        sys.stdin = io.StringIO("2000.00\n")
        self.ops.debit()
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__
        self.assertIn("Insufficient funds for this debit.", captured.getvalue())

if __name__ == "__main__":
    unittest.main()
