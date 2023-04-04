"""A number-guessing game."""

import random

print("Hello there!")
name = input("What is your name? ")
print(f"{name}, I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
guess =  None
tries = 0

while guess != number:
    while True:
        try:
            guess = int(input("What is your guess? "))
            break
        except ValueError:
            print("Nice try but no. That's not an integer. Try again.")

    if guess > 100 or guess < 1:
        print("Did you read? That is not within range. Please try again.")
        continue

    tries += 1
    if guess > number:
        print("Your guess is too large. Please try again.")
    elif guess < number:
        print("Your guess is too low. Please try again.")
    else:
        print(f"Bingo! You guessed the number in {tries} tries!")