#Number Guessing Game
import random

number = random.randint(1, 20)
attempts = 5

print("Welcome to guessing game, you have 5 chances to guess!")

while guess != number and attempts > 0:
    guess = int(input("Enter your guess between 1 and 20: "))
    attempts -= 1

    if guess == number:
        print("Correct guess!")
    else:
        print("Wrong guess!")

if guess != number:
    print(f"Out of attempts! The number was {number}.")
