import random,time

def userIns():
    magicNo = int(input("Enter The Secret Number : "))
    nofTries = int(input("Number of maximum tries : "))
    startp = magicNo-10
    endp = magicNo+10
    return startp,endp,magicNo,nofTries

def guessing():
    sta_t,en_d,SecreT,noftries = userIns()
    guess = random.randint(sta_t,en_d)
    guess_count = 0

    while True:
        if guess_count < noftries:
            guess_count += 1
            print(f"\nGuess = {guess} , Guess Count = {guess_count}\n")
            time.sleep(1.3)
            if guess == SecreT:
                print(f"XXX|| Secret Number is {guess} ||XXX")
                break
            else:
                if guess > SecreT:
                    guess -= 1
                else:
                    guess += 1
        else:
            print(f"Computer Lost! ,couldn't guess it in {noftries} tries.")
            break


def main():
    guessing()

if __name__ == '__main__':
    main()