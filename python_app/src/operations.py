from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.data_program import DataProgram

class Operations:
    """
    Provides account operations: view balance, credit, and debit.
    """
    def __init__(self, data_program: 'DataProgram') -> None:
        """
        Initialize Operations with a DataProgram instance.
        Args:
            data_program (DataProgram): The data storage handler.
        """
        self.data_program: 'DataProgram' = data_program

    def total(self) -> None:
        """
        Display the current account balance.
        """
        balance: float = self.data_program.read()
        print(f"Current balance: {balance:.2f}")

    def credit(self) -> None:
        """
        Prompt for a credit amount, add it to the balance, and display the new balance.
        """
        amount: float = float(input("Enter credit amount: "))
        balance: float = self.data_program.read()
        balance += amount
        self.data_program.write(balance)
        print(f"Amount credited. New balance: {balance:.2f}")

    def debit(self) -> None:
        """
        Prompt for a debit amount, subtract it from the balance if sufficient funds exist, and display the result.
        """
        amount: float = float(input("Enter debit amount: "))
        balance: float = self.data_program.read()
        if balance >= amount:
            balance -= amount
            self.data_program.write(balance)
            print(f"Amount debited. New balance: {balance:.2f}")
        else:
            print("Insufficient funds for this debit.")
