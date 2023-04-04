"""A number-guessing game."""

import random

print("Hello there!")
name = input("What is your name? ")
print(f"{name}, I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
guess =  None
tries = 0

while guess != number:
    guess = int(input("What is your guess? "))
    tries += 1
    if guess > number:
        print("Your guess is too large. Please try again.")
    elif guess < number:
        print("Your guess is too low. Please try again.")
    else:
        print(f"Bingo! You guessed the number in {tries} tries!")