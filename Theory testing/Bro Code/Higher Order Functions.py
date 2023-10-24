#Higher order function = a function that either :
                                # 1.Accept a function as an argument
                                #           or
                                #2.Returns a function

# ex :  1.Accept a function as an argument

def up (text):         #this will make input upper case
    return text.upper()
def low (text):        #this will make input upper case
    return text.lower()

def hello (func):  #This will take text and loud or quiet as arguments
    text = func("HeLLow WoRlD")
    return text

hello(up)       #because of this function accept other functions as arguments this is a higher order function
hello(low)
#----------------------------------------------------------------

#ex :  2.Returns a function

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))