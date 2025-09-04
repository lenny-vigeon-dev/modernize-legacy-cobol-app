from src.const import BALANCE_FORMAT

def write_number(num: float) -> str:
    return f"{num:{BALANCE_FORMAT}}"
