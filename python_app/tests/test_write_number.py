import unittest
from src.write_number import write_number

class TestWriteNumber(unittest.TestCase):
    def test_1000(self):
        # Capture print output
        self.assertEqual(write_number(1000), "001000.00")

    def test_0(self):
        # Capture print output
        self.assertEqual(write_number(0), "000000.00")

    def test_1234_56(self):
        # Capture print output
        self.assertEqual(write_number(1234.56), "001234.56")

    def test_0_68(self):
        # Capture print output
        self.assertEqual(write_number(0.68), "000000.68")


if __name__ == "__main__":
    unittest.main()
