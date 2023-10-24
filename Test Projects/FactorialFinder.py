# what is factorial :
    # factorial of 4 is -->  4! --> 4*3*2*1 = 24

def factorial():
    factorial = 1
    for val in k:
        factorial = val * factorial
    return factorial
value = input("Enter a number to generate factorial : ")
k = []
try:
    value = int(value)
    k.append(value)
    while True:
        value = value -1
        if value == 0:
            break
        k.append(value)
    print(factorial())
except ValueError:
    print("Value Error,Make sure to enter a number not symbols or characters")