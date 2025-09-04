from src.data_program import DataProgram
from src.operations import Operations
from src.const import MENU, PROMPTS, FULL_MENU

def main():
    data_program: DataProgram = DataProgram()
    operations: Operations = Operations(data_program)
    run: bool = True

    while run:
        print(FULL_MENU)
        choice: str = input(PROMPTS["choice_prompt"])

        if choice == "1":
            operations.total()
        elif choice == "2":
            operations.credit()
        elif choice == "3":
            operations.debit()
        elif choice == "4":
            run = False
        else:
            print(MENU["invalid_choice"])

    print(MENU["goodbye"])

if __name__ == "__main__":
    main()
