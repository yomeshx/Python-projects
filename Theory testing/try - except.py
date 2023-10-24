user_file = input("Input your user File.\n")
try:
    f_handle = open(user_file)
    for line in f_handle:
        line=line.lstrip()
        print(line)
except:
    print("File can't be opened !")
    exit() #or quit()

#---------------------------------------CS50p note----------------------------------------------------

#In Python try and except are ways of testing out user input before something goes wrong.

try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
#Notice how, running this code, inputting 50 will be accepted. However, typing in cat will produce an error visible to the user, instructing them why their input was not accepted.
#This is still not the best way to implement this code. Notice that we are trying to do two lines of code. For best practice, we should only try the fewest lines of code possible that we are concerned could fail.

try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
# Notice that while this accomplishes our goal of trying as few lines as possible, we now face a new error! We face a NameError where x is not defined. Look at this code and consider: Why is x not defined in some cases?
# Indeed, if you examine the order of operations in x = int(input("What's x?")), working right to left, it could take an incorrectly inputted character and attempt to assign it as an integer. If this fails, the assignment of the value of x never occurs. Therefore, there is no x to print on our final line of code.


#       - else -
# It turns out that there is another way to implement try that could catch errors of this nature.
#if there is no any exception else will run after try.if there is a exception else won't run


try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# Notice that if no exception occurs, it will then run the block of code within else. Running python number.py and supplying 50, you’ll notice that the result will be printed. Trying again, this time supplying cat, you’ll notice that the program now catches the error.
# Considering improving our code, notice that we are being a bit rude to our user. If our user does not cooperate, we currently simply end our program. Consider how we can use a loop to prompt the user for x and if they don’t prompt again!

while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
# Notice that while True will loop forever. If the user succeeds in supplying the correct input, we can break from the loop and then print the output. Now, a user that inputs something incorrectly will be asked for input again.

# Surely, there are many times that we would want to get an integer from our user.

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()
# Notice that we are manifesting many great properties. First, we have abstracted away the ability to get an integer. Now, this whole program boils down to the first three lines of the program.
# Even still, we can improve this program. Consider what else you could do to improve this program.

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main()
# Notice that return will not only break you out of a loop, but it will also return a value.
# Some people may argue you could do the following:

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            print("x is not an integer")


main()
# Notice this does the same thing as the previous iteration of our code, simply with fewer lines.

#         --pass--
# We can make it such that our code does not warn our user, but simply re-asks them our prompting question by modifying our code as follows:

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            pass


main()
# Notice that our code will still function but will not repeatedly inform the user of their error. In some cases, you’ll want to be very clear to the user what error is being produced. Other times, you might decide that you simply want to ask them for input again.
# One final refinement that could improve the implementation of this get_int function. Right now, notice that we are relying currently upon the honor system that the x is in both the main and get_int functions. We probably want to pass in a prompt that the user sees when asked for input. Modify your code as follows.

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()