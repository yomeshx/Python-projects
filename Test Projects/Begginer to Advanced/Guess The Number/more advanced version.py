import random,sys


print("\n------->| Guess The Number |<-------\n")
print("Secret Number Is Between 1 and 20\n")

def game():
    secretNumber=rand_int()

    for _ in range(5):  #runs 5 times
        userIn=input("Guess the Number : ")

        in_valid = inp_valid(userIn)
        if in_valid == 'con':
            continue
        else:
            userIn=int(userIn)

        if userIn > secretNumber:
            print("Too High!")
        elif userIn < secretNumber:
            print("Too Low!")
        else:
            break

    if userIn == secretNumber:
        print(f"You Won ! The secret number was {secretNumber}")
        terReq()
    else:
        print("\n--->|  All attemps failed ! |<---")
        print(f"Secret Number Was {secretNumber}.")
        terReq()

def terReq(): #termination or continue to play input request
    plagain =input("\nWould you like to try again ? (any/no): ")
    print("")
    if plagain== "no":
        sys.exit()
    else:
        game()

def inp_valid(userIn): #input validation
    if not userIn.isdigit():
        print("Invalid Input !")
        return 'con'

def rand_int():
    secretNumber=random.randint(1,20) #random int
    return secretNumber



if __name__ == '__main__' :
    game()