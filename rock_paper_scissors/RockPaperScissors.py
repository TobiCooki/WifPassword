import random

def main():

    computer_choices = ("rock", "paper", "scissors")
    computer_choice = random.choice(computer_choices)

    print("rock paper scissors, you got this")

    player_choice = input("rock paper or scissors: ")

    print("computer chose: " + computer_choice)

    if computer_choice == player_choice:
        print("we chose the same thing! its a draw."), exit(0)

    while player_choice == "rock":
        if computer_choice == "scissors":
            print("I chose scissors, gg!"), exit(0)
        else:print("I chose paper, I won"), exit(0)

    while player_choice == "paper":
        if computer_choice == "rock":
            print("I chose rock, gg"), exit(0)
        else:print("I chose scissors, I won!"), exit(0)

    while player_choice == "scissors":
        if computer_choice == "paper":
            print("I chose paper, gg!"), exit(0)
        else:print("I chose rock, I won"), exit(0)

main()
