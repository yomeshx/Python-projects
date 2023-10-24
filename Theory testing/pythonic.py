#Python community call "pythonic" when we use features and technics that are unique in python language to solve a problem

#Solution 1 - traditional way of solving a problem
#--------------------------------------

def is_even(n): #we return boolean value as the return value of this function
    if n % 2 == 0:
        return True
    else:
        return False

#Solution 2 - PYTHONIC way of writing the same code above
#--------------------------------------
def is_even(n):
    return True if n % 2 == 0 else False

##Solution 3 - More shorter PYTHONIC way of writing the same code
#--------------------------------------
def is_even(n):
    return n % 2 == 0   
    #because n % 2 == 0 becomes Boolean value anyway we don't even need if conditions
    #-we will need if condition if we return something else like string if this become True or False
    #-ex : return "Hello" if n % 2 == 0 else "Bye"