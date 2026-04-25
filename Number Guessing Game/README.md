# Number Guessing Game

## Description
A simple command-line number guessing game built in Python. The computer picks a random number between 1 and 100. You have **10 attempts** to guess it, with 'Too low' or 'Too high' hints after each guess. Win by guessing correctly; lose if attempts run out.

## Features
- **Random Number Generation**: Secret number between 1 and 100 using `random.randint`.
- **Limited Attempts**: Max 10 guesses with attempt counter; lose if exceeded.
- **Interactive Gameplay**: Real-time feedback ('Too low'/'Too high').
- **Win/Loss Conditions**: Congrats with attempt count on win; reveals number on loss.
- **Input Validation**: Handles non-integer inputs gracefully with error message.
- **No Dependencies**: Pure Python, runs anywhere with Python 3.

## Installation
1. Ensure Python 3 is installed (`python --version`).
2. No additional packages needed!

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Usage](#usage)
- [Example Runs](#example-run-win)
- [Code Structure](#code-structure)
- [License](#license)

## Installation
1. Ensure Python 3 is installed (`python --version`).
2. No additional packages needed!

## How to Play
1. Run the game.
2. Guess a number between 1 and 100.
3. Get hints: "Too low!" or "Too high!".
4. Use up to 10 attempts.
5. Win: Correct guess → see attempts used.
6. Lose: 10 fails → number revealed.

## Usage
From project root:
```
cd "Number Guessing Game"
python Number_Guessing_Game.py
```


### Example Run (Win)
```
Welcome to the Number Guessing Game!
The number is between 1 and 100
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 42
Congratulations! You've guessed the number 42 in 3 attempts!
```

### Example Run (Loss after 10 attempts)
```
... (after 10 wrong guesses)
Sorry, you've used all 10 attempts. The number was 73. Better luck next time!
```

## Code Structure
Key parts in `Number_Guessing_Game.py`:
- `import random`: Generates secret number.
- `attempts = 0; max_attempts = 10`: Tracks guesses.
- `while attempts < max_attempts`: Main loop with `try-except` for input validation.
- `while-else`: Loss message if loop exhausts without break.
- Uses `int(input())` for guesses, compares with hints.

## License
MIT License - feel free to use and modify.

---

Built during python-learning-journey.

## Your Goal (ML Journey)
This game demonstrates foundational Python concepts like loops, conditionals, input handling, and randomness – essential building blocks for machine learning simulations, data generation, and interactive training tools.

