"""A number-guessing game."""

import random

print("Hello there!")
name = input("What is your name? ")
print(f"{name}, I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)