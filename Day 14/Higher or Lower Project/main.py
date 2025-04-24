from art import logo, vs
from random import choice
from game_data import data

def contestant_display(contestant, a_or_b):
    print(f"Compare {a_or_b}: {contestant['name']}, a {contestant['description']}, from {contestant['country']}")

def check_answer(c_s, cont_dic):
    selected_contestant = cont_dic[c_s]
    second_contestant = contestant_b if c_s == "A" else contestant_a
    return selected_contestant['follower_count'] > second_contestant['follower_count']

score = 0
is_game_over = False
contestant_a = choice(data)
while not is_game_over:
    print(logo)

    contestant_b = choice(data)
    if contestant_a == contestant_b:
        contestant_b = choice(data)

    contestant_dic = {
        "A": contestant_a, "B": contestant_b
    }
    if score:
        print(f"You're right! Current score: {score}")
    contestant_display(contestant_a, 'A')
    print(vs)
    contestant_display(contestant_b, 'B')
    choice_selection = input("Who has more followers? Type 'A' or 'B': ")
    is_answer_correct = check_answer(choice_selection, contestant_dic)
    if is_answer_correct:
        score +=1
        contestant_a = contestant_b
    else:
        is_game_over = True
        print("\n"* 20)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    contestant_display(contestant_a, "A")
    print(f"Followers: {contestant_a['follower_count']}")
    print()
    contestant_display(contestant_b, "B")
    print(f"Followers: {contestant_b['follower_count']}")

