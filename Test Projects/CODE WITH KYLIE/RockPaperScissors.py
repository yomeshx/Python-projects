import random

# Game Rules
    #rock > scissors , scissors > paper , paper > scissors
    #if user and computer choose the same thing it's a tie

def winCheck (user,computer):#rock > scissors , scissors > paper , paper > scissors #this function will be used in the function below
    if (user == "r" and computer == "s") or (user == "s" and computer == "p") \
    or (user == "p" and user == "s"):
        return True

def play ():
    userIn = input("Rock (r), Paper (p) or Scissors (s) ? : ").lower()
    computer = random.choice(["r","p","s"])

    if userIn == computer:#if user and computer choose the same thing it's a tie
        return "it's a tie."#note: - whenever the code reaches the return statement its ends the function and return the value


    if winCheck (userIn,computer): #Literal meaning :- if winCheck is true things under this statement will run
        return f"You won! it was {computer}"#note: - whenever the code reaches the return statement its ends the function and return the value
    

    return f"You lost! it was {computer}"#reason there's no need to put else statement is,this function came this far 
                        #-because if conditions above never came True and never lead to the return which exit the function
while True:
    print(play())