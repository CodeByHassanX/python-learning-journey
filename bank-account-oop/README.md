# Bank Account (OOP)

## Description
A simple command-line bank account system built in Python to demonstrate **Object-Oriented Programming (OOP)** concepts. It uses a `bank_account` class to encapsulate account data (name, balance) and behaviors (deposit, withdraw, display). The program runs interactively via a menu loop, allowing users to manage a single account session.

## Features
- **Class-Based Design**: `bank_account` class encapsulates state and methods.
- **Deposit**: Add funds to the account balance.
- **Withdraw**: Remove funds with an overdraft check (insufficient balance protection).
- **Display**: Show current account holder name and balance.
- **Interactive Menu**: Simple numbered menu loop for continuous interaction.
- **Input Validation**: Withdrawal blocked if amount exceeds balance.
- **No Dependencies**: Pure Python, runs anywhere with Python 3.

## Installation
1. Ensure Python 3 is installed (`python --version`).
2. No additional packages needed!

## Usage
Run the bank account program from the project root:
```
cd bank-account-oop
python bank-account.py
```

## Example Run
```
enter your nameAlice
enter your balance1000
1.deposit
2.withdraw
3.display
4.exit
enter your choice1
enter the amount to deposit500
money deposit 500
1.deposit
2.withdraw
3.display
4.exit
enter your choice2
enter the amount to withdraw200
money withdrawn 200
1.deposit
2.withdraw
3.display
4.exit
enter your choice3
Account holder: Alice
Balance: 1300
1.deposit
2.withdraw
3.display
4.exit
enter your choice4
```

## Code Structure
Key parts in `bank-account.py`:
- `class bank_account`: Defines the account with `__init__`, `deposit`, `withdraw`, and `display` methods.
- `deposit(self, amount)`: Increases balance and prints confirmation.
- `withdraw(self, amount)`: Checks balance before decreasing; prints error if insufficient.
- `display(self)`: Prints formatted account details.
- Main `while True` loop: Displays menu, reads user choice, and calls the appropriate method.

## License
MIT License - feel free to use and modify.

---

Built during python-learning-journey.

## Your Goal (ML Journey)
This project demonstrates foundational **Object-Oriented Programming** principles—encapsulation, methods, and state management—which are essential for structuring complex Machine Learning code. OOP skills help in designing modular models, organizing datasets as objects, and building reusable training pipelines in larger ML projects.

