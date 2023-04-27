# This code is a simple math quiz game that generates random numbers and asks the user to solve an addition or
# subtraction problem based on the user's choice
# 4/27/2023
# CTI-110 P5HW - Math Quiz
# Shawnrell Small



# Imports random module
import random
# Defines Menu function
def menu():
    print("Welcome to Math Quiz\nMain Menu\n------------------------------")
    print("1. Adding random numbers\n2. Subtracting random numbers\n3. Exit")
# Defines and generates two random numbers
def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2
# Defines function add_numbers
def add_numbers():
    num1, num2 = generate_numbers()
    correct_answer = num1 + num2
    guess = None
    num_guesses = 0
# while/if loop to define answers
    while guess != correct_answer:
        guess = int(input(f"  {num1} \n +{num2}\n Enter Answer:"))
        num_guesses += 1
        if guess == correct_answer:
            print(f"Congratulations!!! Your answer is correct.\n Number of guesses: {num_guesses}")
        elif guess < correct_answer:
            print(f"Try again:{guess} \nSorry, guess is too low.")
        else:
            print(f"Try again:{guess} \nSorry, guess is too high.")
# Defines function Subtract_numbers
def subtract_numbers():
    num1, num2 = generate_numbers()
    correct_answer = num1 - num2
    guess = None
    num_guesses = 0
    while guess != correct_answer:
        guess = int(input(f"What is the difference between {num1} and {num2}? "))
        num_guesses += 1
        if guess == correct_answer:
            print(f"Congratulations!!! Your answer is correct.\n Number of guesses: {num_guesses}.")
        elif guess < correct_answer:
            print(f"Try again:{guess} \nSorry, guess is too low.")
        else:
            print(f"Try again:{guess} \nSorry, guess is too high.")
# Displays Menu choices using while loop that runs as long as user does not choose 3
choice = None
while choice != "3":
    menu()
    choice = input("Please choose one of the menu options: ")
    if choice == "1":
        add_numbers()
    elif choice == "2":
        subtract_numbers()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice. Please choose again.")