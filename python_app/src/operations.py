from src.data_program import DataProgram
from src.write_number import write_number
from src.const import MESSAGES, PROMPTS

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
        print(MESSAGES["current_balance"].format(write_number(balance)))

    def credit(self) -> None:
        """
        Prompt for a credit amount, add it to the balance, and display the new balance.
        """
        amount: float = float(input(PROMPTS["credit"]))
        balance: float = self.data_program.read()
        balance += amount
        self.data_program.write(balance)
        print(MESSAGES["amount_credited"].format(write_number(balance)))

    def debit(self) -> None:
        """
        Prompt for a debit amount, subtract it from the balance if sufficient funds exist, and display the result.
        """
        amount: float = float(input("Enter debit amount: "))
        balance: float = self.data_program.read()
        if balance >= amount:
            balance -= amount
            self.data_program.write(balance)
            print(MESSAGES["amount_debited"].format(write_number(balance)))
        else:
            print(MESSAGES["insufficient_funds"])
