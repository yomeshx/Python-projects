import random

def guess(x):
    randomNumber = random.randint(1,x) # the value of the random number will be between 1 and x
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"Guess a number between '1' and '{x}' : "))
        if guess > x:
            print(f"Guess should be below {x}")
            continue
        elif guess > randomNumber:
            print("Too High!")
        elif guess < randomNumber:
            print("Too Low!")
        # elif guess == randomNumber:              # one method to show the right guess
        #     print("** You Guessed It! **")
    print(f"You Guessed It! it is {randomNumber}")# second method to show the right guess
    #when guess == randomNumber it breaks the loop and print that you guessed it

guess(10)