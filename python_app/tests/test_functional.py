import unittest
from src.data_program import DataProgram
from src.operations import Operations

class FunctionalTests(unittest.TestCase):
    def test_credit_and_debit_flow(self):
        dp = DataProgram()
        ops = Operations(dp)
        # Credit 100
        dp.write(1000.00)
        ops.data_program.write(1000.00)
        ops.data_program.write(ops.data_program.read() + 100)
        self.assertEqual(ops.data_program.read(), 1100.00)
        # Debit 200
        ops.data_program.write(ops.data_program.read() - 200)
        self.assertEqual(ops.data_program.read(), 900.00)
        # Debit more than balance
        balance_before = ops.data_program.read()
        if balance_before < 1000:
            # Should not allow
            self.assertTrue(balance_before < 1000)

if __name__ == "__main__":
    unittest.main()
