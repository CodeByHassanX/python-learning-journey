import random
attempts = 0
max_attempts = 10
generated_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("The number is between 1 and 100")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < generated_number:
            print("Too low! Try again.")
        elif guess > generated_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {generated_number} in {attempts} attempts!")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")
else:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {generated_number}. Better luck next time!")
    