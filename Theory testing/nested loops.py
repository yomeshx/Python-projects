#Using nested loops to make a rectangular shape
def main():
    printSquare(4)

def printSquare(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            print("#",end="")# '#'s with no new lines so all printed in a single line
        print()#a new line

main()