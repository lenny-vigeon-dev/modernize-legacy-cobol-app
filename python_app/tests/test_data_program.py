import unittest
from src.data_program import DataProgram
from src.const import INITIAL_AMOUNT

class TestDataProgram(unittest.TestCase):
    def setUp(self):
        self.dp = DataProgram()

    def test_initial_balance(self):
        self.assertEqual(self.dp.read(), INITIAL_AMOUNT)

    def test_write_and_read_balance(self):
        self.dp.write(500.25)
        self.assertEqual(self.dp.read(), 500.25)

if __name__ == "__main__":
    unittest.main()
