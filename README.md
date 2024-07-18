# CodSoft Python Programming Internship Projects

## Overview
This repository contains the projects I developed during my Python programming internship at CodSoft. These projects include a basic calculator, a password generator, and a rock-paper-scissors game. Each project showcases different aspects of Python programming, including user input handling, conditionals, loops, and the use of Python libraries.

## Projects

### 1. Basic Calculator
A simple command-line calculator that performs basic arithmetic operations.

#### Features
- Supports addition, subtraction, multiplication, and division.
- Handles division by zero with an error message.
- Allows users to exit the calculator by typing 'exit'.

#### Usage
Run the script and follow the prompts to enter two numbers and an operator (`+`, `-`, `*`, `/`). Type 'exit' to quit the calculator.

```python
while True:
    num1 = int(input("Enter first value: "))
    num2 = int(input("Enter second value: "))
    opr = input("Enter the Operator (+, -, *, /) or 'exit' to quit: ")

    if opr == 'exit':
        print("Calculator exiting...")
        break
    
    if opr in ['+', '-', '*', '/']:
        if opr == '+':
            print(f"Result: {num1 + num2}")
        elif opr == '-':
            print(f"Result: {num1 - num2}")
        elif opr == '*':
            print(f"Result: {num1 * num2}")
        elif opr == '/':
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                print(f"Result: {num1 / num2}")
    else:
        print("Invalid Operator")
```

### 2. Password Generator
A script that generates a random password based on user-specified length.

#### Features
- Includes lowercase and uppercase letters, digits, and punctuation.
- Randomly shuffles characters to ensure a strong, random password.

#### Usage
Run the script and enter the desired password length when prompted. The script will output a random password of the specified length.

```python
import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("Enter password length\n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)

    print("your password is:")
    print("".join(s[0:plen]))
```

### 3. Rock-Paper-Scissors Game
A command-line implementation of the classic rock-paper-scissors game.

#### Features
- Allows user to play against the computer.
- Randomly generates computer's move.
- Determines the winner based on traditional rock-paper-scissors rules.
- Allows users to exit the game by typing 'exit'.

#### Usage
Run the script and enter your move (`Rock`, `Paper`, `Scissor`). Type 'exit' to quit the game.

```python
import random

item_list = ["Rock", "Paper", "Scissor"]

while True:
    user_choice = input("Enter your move (Rock, Paper, Scissor) or 'exit' to quit: ").capitalize()

    if user_choice == 'Exit':
        print("Thanks for playing! Goodbye.")
        break

    if user_choice not in item_list:
        print("Invalid move! Please enter Rock, Paper, or Scissor.")
        continue

    comp_choice = random.choice(item_list)

    print(f"\nUser choice = {user_choice}, Computer choice = {comp_choice}")

    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and comp_choice == "Scissor") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissor" and comp_choice == "Paper"):
        print("You win!")
    else:
        print("Computer wins!")
```

## Acknowledgements
- Thanks to CodSoft for the opportunity to develop these projects during my internship.
- Special thanks to the Python community for providing excellent resources and support.


