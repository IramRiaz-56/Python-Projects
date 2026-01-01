# Python program for the Number Guessing Game

import random
print("Welcome to the Number Guessing Game!")           #Program to let the user guess a random number within range
secret_number = random.randint(1, 10)                    #Generate a random number between 1 and 100
attempts = 0  # To count the number of attempts

while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break  # Exit the loop when guessed correctly

    except ValueError:
        print("Please enter a valid integer.")
