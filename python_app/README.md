# Python Account Management App

A modern Python port of the legacy [COBOL](../legacy_cobol_app/README.md) Account Management System. This app lets you view the balance, credit, and debit an in-memory account, with automated tests and coverage.

# Index

- [Prerequisites: Install Python](#prerequisites-install-python)
- [Open this project folder](#open-this-project-folder)
- [Run the program](#run-the-program)
- [(Optional) Run the automated tests](#optional-run-the-automated-tests)
- [Troubleshooting](#help-it-didnt-work)

## Prerequisites: Install Python

You need Python 3.10+.

- Windows
  1) Go to https://www.python.org/downloads/windows/
  2) Click the big yellow “Download Python 3.x.x” button.
  3) Open the downloaded file.
  4) Important: tick “Add python.exe to PATH”.
  5) Click “Install Now” and wait.
  6) Check it worked: open Command Prompt and run:
     ```pwsh
     python --version
     ```
     You should see something like “Python 3.11.x”.

- macOS
  1) Go to https://www.python.org/downloads/macos/
  2) Download the “macOS 64-bit universal2 installer”.
  3) Open the .pkg and install.
  4) Open Terminal and run:
     ```bash
     python3 --version
     ```

- Linux (Ubuntu/Debian)
  ```bash
  sudo apt-get update
  sudo apt-get install -y python3 python3-pip
  python3 --version
  ```

## Open this project folder

Find the folder named `python_app`.

- Windows: open File Explorer, go into `python_app`, click the address bar, type `cmd`, press Enter.
- macOS/Linux: open Terminal and change directory (cd) to the `python_app` folder.

## Run the program

- Windows (PowerShell or Command Prompt):
  ```pwsh
  python .\main.py
  ```

- macOS/Linux (Terminal):
  ```bash
  python3 ./main.py
  ```

You’ll see a menu:
- 1: View Balance
- 2: Credit Account
- 3: Debit Account
- 4: Exit

Type the number and press Enter. To quit, choose 4.

## (Optional) Run the automated tests

Install the small test tool:

- Windows:
  ```pwsh
  python -m pip install -r requirements-test.txt
  ```

- macOS/Linux:
  ```bash
  python3 -m pip install -r requirements-test.txt
  ```

Run all tests:

- Windows:
  ```pwsh
  python -m unittest discover -s tests
  ```

- macOS/Linux:
  ```bash
  python3 -m unittest discover -s tests
  ```

See coverage (how much code was tested):

- Windows:
  ```pwsh
  python -m coverage run -m unittest discover -s tests
  python -m coverage report
  ```

- macOS/Linux:
  ```bash
  python3 -m coverage run -m unittest discover -s tests
  python3 -m coverage report
  ```

## Help! It didn’t work

- “python is not recognized” on Windows? Close and reopen the terminal, then try again. If it still fails, reinstall and tick “Add python.exe to PATH”.
- On macOS/Linux, use `python3` instead of `python`.
- Make sure your terminal is inside the `python_app` folder when running the commands above.
