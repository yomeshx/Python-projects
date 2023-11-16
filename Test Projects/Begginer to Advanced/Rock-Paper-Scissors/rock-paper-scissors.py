#rock paper scissors
#---- game rules ----
    #rock < paper
    #rock > scissors
    #scissors > paper
# game flow
    # 1.input
    # 2. evaluvation 
    # 3. Output



import sys,random

valid_in =["r","p","s"]



def game(player_input):
    randBotchoice = random.choice(valid_in)

    if player_input == randBotchoice:
        print("It's a Tie !")
    
    elif player_input == "r":
        if randBotchoice == "p":
            print("You Lost !   'Your Rock Got Wrapped'")
        elif randBotchoice =="s":
            print("You Won !    'My Rock Defeated Evil Scissor'")
    
    elif player_input == "p":
        if randBotchoice == "r":
            print("You Won ! 'You Wrapped The Rock'")
        if randBotchoice == "s":
            print("You Lost ! 'Your Paper Got Cut By Scissors'")
    else:
        if randBotchoice == "p":
            print("You Won ! 'Paper Got Cut By You'")
        else:
            print("You Lost ! 'Scissors can't cut a Rock'")

def ask_player():
    player = input("\n(R)ock - (P)aper - (S)cissors ?\n----------->| ").lower()
    return player



print("\n<---- Rock Paper Scissors ---->\n\n")


while True:
    for _ in range(5):
        player = ask_player()
        if player not in valid_in:
            print(f"There's no such a option exist !")
        game(player)

    plymr = input("\n    Would you like to exit ?\n\n 'y' to exit or press any key for keep playing ? : ").lower()

    if plymr == 'y':
        sys.exit()
    else:
        continue