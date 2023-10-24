#we can use sys.exit to print something and then exit the program
import sys
if len(sys.argv) < 2:
    sys.exit("Please give an argument")
elif len(sys.argv) > 2:
    sys.exit("Too much arguments")

print("Hi my name is", sys.argv[1])
#we don't need to indent this print to a else because program will be terminated if if,else condition became true
#therefore 