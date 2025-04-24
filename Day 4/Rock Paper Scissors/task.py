import random
rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_Choices = [rock, paper, scissors]

my_choice_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

while my_choice_input > 2 or my_choice_input < 0:
    my_choice_input = int(input("Wrong Selection. Please Type 0 for Rock, 1 for Paper or 2 for Scissors "))

print("My choice ", game_Choices[my_choice_input])
computer_choice = random.randint(0, 2)
print(f"Computer Choice {game_Choices[computer_choice]}")

results = [
    ["It's a Draw", "Computer Won - Paper beats Rock", "You Won - Rock beats Scissors"],
    ["You Won - Paper beats Rock", "It's a Draw", "Computer Won - Scissors beats Paper"],
    ["Computer Won - Rock beats Scissors", "You Won - Scissors beats Paper", "It's a Draw"]
]

print(results[my_choice_input][computer_choice])