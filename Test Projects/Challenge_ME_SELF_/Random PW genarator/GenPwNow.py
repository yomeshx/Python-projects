import random,time


symbolZ = ["!","@","#","$","%","^","&","*","(",")","_","+","=","-","<",">","?","/","|","}","{","[","]","}"]
Uch = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Lch =list()

ul = []
ll = []
sy = []
level01 = []

for ch in Uch: #making a lowercase character list using uppercase letters
    ch = ch.lower()
    Lch.append(ch)

#-----------------------------------------------------------------------------------------------------------------

def randomizer():
    for x in range(2):
        pas = random.choice(Uch)
        ul.append(pas)

    for y in range(2):
        pas = random.choice(Lch)
        ll.append(pas)

    for z in range(3):
        pas = random.choice(symbolZ)
        sy.append(pas)

    optionL = [ul,ll,sy]
    for n in range(3):
        ranOp = random.choice(optionL)
        for n in range(2):
            obJct = random.choice(ranOp)
            level01.append(obJct)
        optionL.remove(ranOp)

    return level01
#-----------------------------------------------------------------------------------------------------------------
def main():
    # saveFile = open(file="D:\\P\\Programing\\Python\\My Learning Projects\\Challenge_ME_SELF_\\Random PW genarator\\SavedPWs.txt")
    # pwNo = 0
    while True:
        lenOfPw = input("\nEnter Length of the password(Must be 4 or above 4)              - ENTER 'E' to Exit -\n|--------------------------->> : ")
        pw =""
        if lenOfPw.isdigit():
            for t in range(int(lenOfPw)):
                obl = randomizer()
                tf = random.choice(obl)
                pw = pw+tf #actual PW
            # pwNo_and_pw = str(pwNo+1) + ". | " +pw # To write to the text file
            # saveFile.write(pwNo_and_pw)
            # saveFile.close()
            print(f"\nNew Password : {pw}\n\n")
            break
        elif lenOfPw == "E" or lenOfPw== "e":
            quit()
        else:
            print("\nWrong input.Try Again!")
            continue
    #commented out lines are an attempt to write generated PWs into a text file . but didn't work
#-----------------------------------------------------------------------------------------------------------------
while True:
    main()
    time.sleep(0.1)