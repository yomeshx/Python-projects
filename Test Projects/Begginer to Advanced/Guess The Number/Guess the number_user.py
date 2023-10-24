import random

start_range = int(input("Starting from ? : "))
end_range = int(input(f"From {start_range} to ? : "))
# print(start_range,"",end_range)   #testing

rand_num = random.randint(start_range,end_range)

while True:
    userGuess = int(input("Take a guess : "))
    try:
        if end_range<userGuess or userGuess<start_range:
            print("Not in Range ! ,Try Again !")
            continue
        elif userGuess == rand_num:
            print(f"Yes ! You Won ! {rand_num} is the Secret Number")
            break
        else:
            print("Try Again !")
    except ValueError:
        print("Invalid input, please only enter Numbers")
        continue