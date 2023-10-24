#we can use while loop to ask input until valid input is given
while True:
    inp = int(input("Enter a number : "))
    if inp > 0:
        break

while True: #same thing above
    inp = int(input("Enter a number : "))
    if inp < 0:
        continue