from src.const import MAX_AMOUNT
from src.data_program import DataProgram
from src.write_number import write_number

class Operations:
    """
    Provides account operations: view balance, credit, and debit.
    """
    def __init__(self, data_program: DataProgram) -> None:
        """
        Initialize Operations with a DataProgram instance.
        Args:
            data_program (DataProgram): The data storage handler.
        """
        self.data_program: DataProgram = data_program

    def total(self) -> None:
        """
        Display the current account balance.
        """
        balance: float = self.data_program.read()
        print(f"Current balance: {write_number(balance)}")

    def credit(self) -> None:
        """
        Prompt for a credit amount, add it to the balance, and display the new balance.
        """
        amount: float = float(input("Enter credit amount: "))
        balance: float = self.data_program.read()
        if balance + amount < MAX_AMOUNT:
            balance += amount
            self.data_program.write(balance)
        print(f"Amount credited. New balance: {write_number(balance)}")

    def debit(self) -> None:
        """
        Prompt for a debit amount, subtract it from the balance if sufficient funds exist, and display the result.
        """
        amount: float = float(input("Enter debit amount: "))
        balance: float = self.data_program.read()
        if balance >= amount:
            balance -= amount
            self.data_program.write(balance)
            print(f"Amount debited. New balance: {write_number(balance)}")
        else:
            print("Insufficient funds for this debit.")
