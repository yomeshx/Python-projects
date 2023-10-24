import random

n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed :
    guess = int(input("\n\nGuess the number !!!\n\n"))
    if guess > 0:

        if guess > to_be_guessed:
            print("\nNumber is too large !!!\n")
        elif guess < to_be_guessed:
            print("\nNumber is too small !!!\n")
    else:
        print("\nSorry that you are giving up !\n")
        break

print("\nCongrats!!! You are correct !!!\n")