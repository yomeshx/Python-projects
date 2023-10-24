import re

while True:
    email = input("Enter your Email : ")

    if re.search(r"^.+@.+\.edu$",email):#True if one or more character before and after @ sign and ends with .edu
        print("Valid!")
    else:
        print("Invalid")
        break

#----------------------------------------------------------------------------------------------------------------------------
import re

while True:
    email = input("Enter your Email : ")

    # if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email): #longer
    if re.search(r"^\w+@\w+\.edu$",email):                       #shortened by w
        print("Valid!")
    else:
        print("Invalid")
        break
