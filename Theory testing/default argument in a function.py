#default argument is assigned to the parameter when we "define" the function. note(when 'calling' the function assigning values are called keyword args.don't confuse it with this)
#it is used in case when calling the function it didn't received any argument or user forget to to give an argument to the function .
# -we can set up a default value.

def hello (name="johnDoe"):
    print(f"Hello {name}")

hello("yomesh") #gave an argument
hello() #didn't gave an argument so function used the default argument