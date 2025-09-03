# COBOL to Python Migration

Quick links:
- Non-technical users: start with the Python app guide at [python_app/README.md](./python_app/README.md)
- COBOL project guide: [legacy_cobol_app/README.md](./legacy_cobol_app/README.md)
- Test plan: [legacy_cobol_app/TESTPLAN.md](./legacy_cobol_app/TESTPLAN.md)

# COBOL to Python Migration Guide

This document explains the process and decisions made during the migration of the legacy COBOL account management system to a modern Python implementation.

## Overview

The original COBOL application consisted of three main files:
- `main.cob`: User interface and main program loop
- `operations.cob`: Account operations (view, credit, debit)
- `data.cob`: Data storage and retrieval

The Python version replicates this structure with:
- `main.py`: Main program logic and user interface
- `src/operations.py`: Account operations as a class
- `src/data_program.py`: Data storage as a class

## Migration Steps

1. **Analysis of COBOL Logic**
   - Identified program flow, data structures, and operations.
   - Mapped COBOL constructs (PERFORM, CALL, MOVE, etc.) to Python equivalents.

2. **Design in Python**
   - Used classes to encapsulate data and operations.
   - Replaced COBOL's procedural flow with Python's object-oriented approach.
   - Used Python's input/output functions for user interaction.

3. **Implementation**
   - Created `DataProgram` class for balance storage and retrieval.
   - Created `Operations` class for account actions (view, credit, debit).
   - Implemented a main loop in `main.py` for user interaction.
   - Added type hints and docstrings for clarity and maintainability.
   - Python supports > 1 million number where Cobol had undefined behaviour.

4. **Testing**
   - Python application: unit and functional tests under `python_app/tests` using `unittest`.
   - Simulated user input for interactive flows and validated stdout.
   - Code coverage via `coverage.py` with a CI gate (see CI below).
   - COBOL application: functional, black‑box tests via Python runner in `legacy_cobol_app/test_cobol_operations.py` (executes the compiled COBOL binary and asserts output).
   - Tests cover the business cases listed in [TESTPLAN.md](./legacy_cobol_app/TESTPLAN.md).

### Continuous Integration (CI)

We run Python tests in CI across multiple Python versions with a coverage threshold:
- Workflow: [.github/workflows/python_test.yml](./.github/workflows/python_test.yml)
- Triggers: push to `main` and `dev`, and pull requests to `main`.
- Matrix: Python 3.8 through 3.13 on Ubuntu runners.
- Coverage gate: build fails if TOTAL coverage < 95%.


## Key Differences

- **Procedural vs. Object-Oriented**: COBOL is procedural; Python implementation uses classes and methods.
- **Data Handling**: COBOL uses fixed-size fields; Python uses dynamic types and variables.
- **User Interaction**: COBOL uses DISPLAY and ACCEPT; Python uses `print()` and `input()`.
- **Testing**: Python supports automated testing and coverage tools, improving reliability.

## Benefits of Migration

- Improved code readability and maintainability.
- Easier to extend and test.
- Modern tooling and ecosystem support.

## Next Steps

- Further refactor for scalability or integration with databases.
- Add more robust error handling and logging.
- Consider packaging as a module or web service if needed.

## How to run and test (summary)

Non‑technical users: please follow the step‑by‑step guide in [python_app/README.md](./python_app/README.md).

Technical summary:
- Python app
   - Run: `cd python_app` then `python main.py` (Windows) or `python3 main.py` (macOS/Linux).
   - Tests: `python -m unittest discover -s tests`.
   - Coverage: `python -m coverage run -m unittest discover -s tests && python -m coverage report`.
- COBOL app
   - Compile (GnuCOBOL): `cobc -x legacy_cobol_app/main.cob legacy_cobol_app/operations.cob legacy_cobol_app/data.cob -o legacy_cobol_app/accountsystem`.
   - Functional tests: from `legacy_cobol_app`, ensure `accountsystem(.exe)` exists, then `python test_cobol_operations.py`.

For any questions or further improvements, refer to the linked READMEs and code comments.
