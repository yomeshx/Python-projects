# You can create optional arguments/variables when creating a function.
#you do that by assigning a default variable incase user didn't gave a value to the optional variable
# ex 1
def details(name,age,phone=None): #here we made giving phone number optional. if not given it will be None 
    pass

# ex 2
def details(name,age,phone="0750000000"): #here we made giving phone number optional. if not given it will be 0750000000
    print(f"{name} is {age}, call him - {phone}")

def main():
    name = input("Name : ")
    age = int(input("Age: "))
    phone = input("Phone: ")
    if phone =="":
        details(name,age)
    else:
        details(name,age,phone)

if __name__ == "__main__":
    main()