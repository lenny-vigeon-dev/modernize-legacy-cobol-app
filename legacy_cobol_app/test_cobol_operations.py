import unittest
import subprocess
import os
import shutil


class TestCobolMain(unittest.TestCase):
    exe_path: str = ""

    @classmethod
    def setUpClass(cls) -> None:
        # Resolve the accountsystem executable in the current folder
        base = "accountsystem"
        candidate = base + ".exe" if os.name == "nt" else "./" + base
        # Try absolute path in cwd
        if os.name == "nt":
            path = os.path.join(os.getcwd(), base + ".exe")
        else:
            path = os.path.join(os.getcwd(), base)
        if os.path.exists(path):
            cls.exe_path = path
        elif shutil.which(candidate):
            cls.exe_path = shutil.which(candidate)  # type: ignore
        else:
            cls.exe_path = ""

    def run_accounts(self, *inputs: str) -> str:
        if not self.exe_path:
            self.skipTest("accounts system executable not found. Compile 'main.cob' to 'accountsystem(.exe)' first.")
        input_str = "\n".join(inputs) + "\n"
        result = subprocess.run(
            [self.exe_path],
            input=input_str,
            capture_output=True,
            text=True,
        )
        # For debugging on failure, you may inspect result.stderr as well
        return result.stdout

    def test_view_balance_and_exit(self):
        out = self.run_accounts("1", "4")
        self.assertIn("Account Management System", out)
        self.assertIn("Current balance:", out)
        self.assertIn("Exiting the program. Goodbye!", out)

    def test_invalid_entry(self):
        out = self.run_accounts("0", "5", "a", "4")
        # At least three invalid prompts
        self.assertGreaterEqual(out.count("Invalid choice"), 3)
        self.assertIn("Exiting the program. Goodbye!", out)

    def test_add_credit(self):
        out = self.run_accounts("2", "500", "4")
        self.assertIn("Amount credited. New balance:", out)
        self.assertIn("Exiting the program. Goodbye!", out)

    def test_debit_credit(self):
        out = self.run_accounts("3", "500", "4")
        self.assertIn("Amount debited. New balance:", out)
        self.assertIn("Exiting the program. Goodbye!", out)

    def test_successive_action(self):
        # Credit 750.23 -> 1750.23, Debit 500.89 -> 1249.34, view, Credit 1_000_000 -> ignored by field size, Debit 1250 -> insufficient, view, exit
        out = self.run_accounts("2", "750.23", "3", "500.89", "1", "2", "1000000", "3", "1250", "1", "4")
        self.assertIn("Amount credited. New balance:", out)
        self.assertIn("Amount debited. New balance:", out)
        self.assertIn("Current balance:", out)
        self.assertIn("Insufficient funds", out)

    def test_exit_direct(self):
        out = self.run_accounts("4")
        self.assertIn("Exiting the program. Goodbye!", out)

    def test_credit_integer_and_view_balance(self):
        # 1000 + 144 = 1144.00
        out = self.run_accounts("2", "144", "1", "4")
        self.assertIn("Amount credited. New balance:", out)
        self.assertTrue("1144.00" in out or "1144" in out)

    def test_credit_decimal_and_view_balance(self):
        # 1000 + 0.75 = 1000.75
        out = self.run_accounts("2", "0.75", "1", "4")
        self.assertIn("Amount credited. New balance:", out)
        self.assertIn("1000.75", out)

    def test_credit_ignore_excess_and_view_balance(self):
        # Crediting 1,000,000 should be ignored (field too small), balance stays 1000.00
        out = self.run_accounts("2", "1000000.00", "1", "4")
        self.assertIn("Amount credited. New balance:", out)
        self.assertIn("Current balance:", out)
        self.assertIn("1000.00", out)

    def test_debit_insufficient_only(self):
        out = self.run_accounts("3", "2000", "4")
        self.assertIn("Insufficient funds", out)

    def test_recover_after_multiple_invalid_then_valid(self):
        out = self.run_accounts("0", "x", "9", "1", "4")
        self.assertGreaterEqual(out.count("Invalid choice"), 3)
        self.assertIn("Current balance:", out)


if __name__ == "__main__":
    unittest.main()
