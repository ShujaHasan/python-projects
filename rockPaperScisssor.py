"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, Paper, Scissor)
2- Computer Choice (computer will choose randomly not conditionally)
3- Result Print

Cases:

A- Rock
Rock - Rock = Tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

B- Paper
Paper - Paper = Tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = Tie
Scissor - Paper = Scissor Win
Scissor - Rock = Rock Win

"""

import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move: Rock, Paper, Scissor = ").capitalize()

comp_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")

if user_choice == comp_choice:
    print("It's a Tie! ")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Wins! ")
    else:
        print("Rock smashes scissor = You win!")


elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper covers Rock = You Wins! ")
    else:
        print("Scissor cuts the paper = Computer Wins!")


elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts the paper = You Win! ")
    else:
        print("Rock smashes scissor = Computer wins!")