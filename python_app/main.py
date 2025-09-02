from src.data_program import DataProgram
from src.operations import Operations

def main():
    data_program: DataProgram = DataProgram()
    operations: Operations = Operations(data_program)
    run: bool = True

    while run:
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")
        choice: str = input("Enter your choice (1-4): ")

        if choice == "1":
            operations.total()
        elif choice == "2":
            operations.credit()
        elif choice == "3":
            operations.debit()
        elif choice == "4":
            run = False
        else:
            print("Invalid choice, please select 1-4.")

    print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()
