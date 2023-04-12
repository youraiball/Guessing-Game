"""A number-guessing game."""

import random

name = input("Hello, let's play a number guessing game. What is your name? ")

while True:
    print(f"{name}, I need a range for the secret number.")
    start = int(input("What is the start of your range? "))
    end = int(input("What is the end of your range? "))
    print(f" Ok {name}, I am thinking of a number between {start} and {end}.")
    number = random.randint(start,end)
    guess = None
    tries = 0
    best_score = 0
    max_tries = 5

    while guess != number:
        if max_tries == 0:
            print("You've reached the limit of tries")
            break

        try:
            guess = int(input("What is your guess? "))
        except (TypeError, ValueError):
            print("You must enter an integer.")
            continue

        if guess < start or guess > end:
            print(f"Thats not within range. Stay between {start} - {end} and guess again")
            continue

        tries += 1
        max_tries -= 1

        if guess > number:
            print("Your guess is too large. Guess again")
        elif guess < number:
            print("Your guess is too small. Guess again")
        elif guess == number:
            # Check if current number of tries is less than the current best score
            # If yes, set best score to current number of tries
            # Account for edge case of first round where best_score is 0
            if best_score == 0:
                best_score = tries
            elif tries < best_score:
                best_score = tries
            print(f"Congrats! You guessed my number in {tries} tries!")
        
    play_again = input("Would you like to play again? Y/N ").upper()
    if play_again == "Y":
        continue
    elif play_again == "N":
        print(f"Thank you for playing. Your best score is {best_score} tries.")
        break


        
            