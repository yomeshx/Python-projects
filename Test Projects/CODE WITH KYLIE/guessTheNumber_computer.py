import random
#Note: you don't say the number to the program its in only your mind
def guessBot(x):#Computer will be the one who will be guessing
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            botGuess = random.randint(low,high)
        else:
            botGuess = high #also can be low because now high == low
        feedback = input(f"Is {botGuess} correct (C) or is it too low (L) or too high (H) : ").lower()
        if feedback == "h":
            high = botGuess - 1
        elif feedback == "l":
            low = botGuess + 1
    print(f"Yeah bitch ! I guessed it. it's {botGuess}")


guessBot(10)