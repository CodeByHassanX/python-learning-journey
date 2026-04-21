def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


while True:

    print("\n--- Calculator Menu ---")
    print("sum, subtract, multiply, divide, power, factorial, gcd, exit")

    make_choice = input("Choose operation: ")

    if make_choice == "exit":
        print("Calculator closed.")
        break

    try:
        if make_choice == "factorial":
            a = int(input("Enter number: "))
            print("Result:", factorial(a))
        else:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))

            if make_choice == "sum":
                print("Result:", sum(a, b))

            elif make_choice == "subtract":
                print("Result:", subtract(a, b))

            elif make_choice == "multiply":
                print("Result:", multiply(a, b))

            elif make_choice == "divide":
                print("Result:", divide(a, b))

            elif make_choice == "power":
                print("Result:", power(a, b))

            elif make_choice == "gcd":
                print("Result:", gcd(a, b))

            else:
                print("Invalid operation")

    except ValueError as e:
        print("Error:", e)