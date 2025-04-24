from random import randint
from art import logo

def compare(u_guess, g_number):
    if user_guess > g_number:
        print("Too high.")
    elif user_guess < g_number:
        print("Too low.")
    else:
        print(f"You got it! The answer was {u_guess}.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':")
lives = 0
if level == 'easy':
    lives = 10
elif level == "hard":
    lives = 5

guessed_number = randint(1, 100)
user_guess = 0
print(f"Guessed number: {guessed_number}")

while guessed_number != user_guess and lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess:"))
    compare(user_guess, guessed_number)
    if user_guess != guessed_number:
        lives -= 1
        if lives == 0:
            print("You've run out of guesses. Refresh the page to run again.")
