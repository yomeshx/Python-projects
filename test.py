def userIns():
    numToguess =input("Number to guess : ")
    starting = 0
    ending = int(numToguess) + 10
    return numToguess,starting,ending

def game(ntg,strt,endin):
    invld = []
    for x in range(strt,endin):
        if x == ntg and:
            print("you won ! Congratulations")
            break
        invld.append(x)