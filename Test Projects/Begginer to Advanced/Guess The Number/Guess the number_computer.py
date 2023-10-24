import random

def userIns():   #Asking the range from user
    secretNumber = int(input("Secret Number : "))
    start_p = secretNumber-10 #for example if the secretNo is 10, start will be 0
    end_p = secretNumber+10   # ,,         ,,          ..       , end will be 20
    return start_p,end_p,secretNumber

def guess(st_rtp,e_dp,secr_tNo):
    secretNumber = secr_tNo
    discard =[]
    guess_count =0
    while True:
        guess = random.randint(st_rtp,e_dp)
        print(guess)
        guess_count +=1
        if guess not in discard: 
            if guess == secretNumber:
                print(f"-:|| Ah..Ha.. it is {guess} ||:-")
                print("--------------------------------------------")
                print(f"Computer Took {guess_count} Guesses !")
                print("Wrong guesses ! ",discard)
                break
            else:
                discard.append(guess)
            

def main():
    startp,endp,secretNo = userIns()
    guess(startp,endp,secretNo)

if __name__ == '__main__':
    main()