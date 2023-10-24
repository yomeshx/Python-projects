import random
import time

choices = ["rock","paper","scissors"]

player = None
while not player == "exit":
    computer = random.choice(choices)
    player = input("\nrock , paper or scissors ? \n").lower()
    if player in choices:
        if player == computer:
            print(f"computer : {computer}")
            print(f"player : {player}")
            print("Tie!")

        elif player == "rock":
            if computer == "paper":
                print(f"computer : {computer}")
                print(f"player : {player}")
                print("You Lose !")
            elif computer == "scissors":
                print(f"computer : {computer}")
                print(f"player : {player}")
                print("You Win !")

        elif player == "paper":
            if computer == "scissors":
                print(f"computer : {computer}")
                print(f"player : {player}")
                print("You Lose !")
            elif computer == "rock":
                print(f"computer : {computer}")
                print(f"player : {player}")
                print("You Win !")

        elif player == "scissors":
            if computer == "rock":
                print(f"computer : {computer}")
                print(f"player : {player}")
                print("You Lose !")
            elif computer == "paper":
                print(f"computer : {computer}")
                print(f"player : {player}")
                print("You Win !")
    else:
        print("Input Not acceptable !")
    time.sleep(2)