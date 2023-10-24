import random,time,sys

#25 words in total
words = ["Chapter","Statement","Tension","Temperature","Excitement","Priority",
         "Dangerous","Alligator","Construction","Electricity","Availability",
         "Resistance","Terrorism","Arguable","Trustworthy","Passenger",
         "Untouchable","Discrimination","Conclusion","Situation","application",
         "Difference","Maintenance","Conversation","Judgment"
         ]

def termination():
    terReq =input("Insert 'E' to exit or 'any key' to play again \n      E/any : ").upper()
    if terReq == "E" :
        print("\nExiting...")
        time.sleep(1)
        sys.exit()
def main():
    while True:
        ch_word = random.choice(words).upper() #Randomly chosen word
        lenWord = len(ch_word)  #Length of the word
        chW_char =[]

        p1 =lenWord - 2
        p2 =lenWord - 3
        p3 =round(lenWord*0.5)
        p4 =p3-2

        for i in ch_word:
            chW_char.append(i)   #storing individual characters in a list

        # print(chW_char)

        chW_char[p1-1] = "_"
        chW_char[p2-1] = "_"
        chW_char[p3-1] = "_"
        chW_char[p4-1] = "_"

        # print(chW_char)

        dword= ""
        for i in chW_char:
            dword +=i

        #print(dword)

        print("\n\n       --- Guess The Word --\n")
        print(f"\n            {dword}                   length of the word = {lenWord}\n")
        Usr_ans = input("What is the word ? -->|:  ").upper()

        try:
            if Usr_ans == ch_word:
                print(f"You Won!, it is {Usr_ans}")
                termination()
            else:
                print("\n\n        Wrong word, Try again!")
                time.sleep(1)
                
        except ValueError:
            print("\n--Invalid Input ,Try again!--")
            termination()

if __name__ == '__main__':
    main()