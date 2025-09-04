# Operation messages
MESSAGES = {
    "current_balance": "Current balance: {}",
    "amount_credited": "Amount credited. New balance: {}",
    "amount_debited": "Amount debited. New balance: {}",
    "insufficient_funds": "Insufficient funds for this debit.",
}

# Input prompts
PROMPTS = {
    "credit": "Enter amount credit: ",
    "debit": "Enter amount debit: ",
    "choice_prompt": "Enter your choice (1-4): "
}

# Main menu constants
MENU = {
    "title": "Account Management System",
    "separator": "--------------------------------",
    "option_1": "1. View Balance",
    "option_2": "2. Credit Account",
    "option_3": "3. Debit Account",
    "option_4": "4. Exit",
    "invalid_input": "Invalid input, please enter a number (1-4).",
    "invalid_choice": "Invalid choice, please select 1-4.",
    "goodbye": "Exiting the program. Goodbye!"
}

FULL_MENU = f"""{MENU['separator']}
{MENU['title']}
{MENU['option_1']}
{MENU['option_2']}
{MENU['option_3']}
{MENU['option_4']}
{MENU['separator']}
"""