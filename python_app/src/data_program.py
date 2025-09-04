from typing import Union

from src.const import INITIAL_AMOUNT

class DataProgram:
    """
    Handles storage and retrieval of the account balance.
    """
    def __init__(self, initial_amount: float = INITIAL_AMOUNT):
        """
        Initialize the DataProgram with a default balance of 1000.00.
        """
        self.storage_balance: float = initial_amount

    def read(self) -> float:
        """
        Returns the current account balance.
        """
        return self.storage_balance

    def write(self, balance: Union[float, int]):
        """
        Updates the account balance to the provided value.
        Args:
            balance (float | int): The new balance to set.
        """
        self.storage_balance = float(balance)
