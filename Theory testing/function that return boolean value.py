# calling function that returns boolean value to trigger a if condition

def main():
    x = int(input("What's x? "))
    if is_even(x): #the return value of is_even is True , if condition will be true and will print("Even")
        print("Even")
    else:
        print("Odd")


def is_even(n): #we return boolean value as the return value of this function
    if n % 2 == 0:
        return True
    else:
        return False


main()
#Notice that one reason our if statement is_even(x) works, even though there is no operator there.
#-This is because our function returns a bool (or boolean), true or false, back to the main function.
#-The if statement simply evaluates whether or not is_even of x is true or false.