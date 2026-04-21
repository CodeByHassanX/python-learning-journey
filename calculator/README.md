# Simple Python Calculator

## Description
A simple command-line calculator built in Python. Supports basic arithmetic operations (sum, subtract, multiply, divide), power, factorial, and greatest common divisor (GCD). Features an interactive menu loop that continues until the user types 'exit'. Includes error handling for division by zero and negative factorial input.

## Features
- **Basic Operations**: sum, subtract, multiply, divide (safe from div/0)
- **Advanced Functions**: power (a^b), factorial (n!), GCD (Euclidean algorithm)
- **Interactive Menu**: Easy-to-use loop interface
- **Error Handling**: Catches ValueErrors and prints user-friendly messages
- **No Dependencies**: Pure Python, runs anywhere with Python 3

## Installation
1. Ensure Python 3 is installed (`python --version`).
2. (Optional) Create virtual environment:
   ```
   python -m venv calc_env
   calc_env\\Scripts\\activate  # Windows
   ```
3. No additional packages needed!

## Usage
Run the calculator:
```
cd c:/Users/Shah/Desktop/Projects/python-learning-journey
python calculator/calculator.py
```

### Example Run
```
--- Calculator Menu ---
sum, subtract, multiply, divide, power, factorial, gcd, exit
Choose operation: sum
Enter first number: 5
Enter second number: 3
Result: 8

--- Calculator Menu ---
sum, subtract, multiply, divide, power, factorial, gcd, exit
Choose operation: factorial
Enter number: 5
Result: 120

--- Calculator Menu ---
sum, subtract, multiply, divide, power, factorial, gcd, exit
Choose operation: divide
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero

--- Calculator Menu ---
sum, subtract, multiply, divide, power, factorial, gcd, exit
Choose operation: exit
Calculator closed.
```

## Code Structure
- Functions defined for each operation with input validation.
- Main `while True` loop handles menu display, input parsing, execution, and exception catching.
- File: `calculator/calculator.py`



## License
MIT License - feel free to use and modify.

---

Built during python-learning-journey.

## Your Goal (ML Journey)
This calculator is part of a Machine Learning journey, demonstrating foundational Python programming skills essential for data manipulation and numerical computations in ML projects.

