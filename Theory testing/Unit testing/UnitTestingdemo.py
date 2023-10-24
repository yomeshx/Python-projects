# Whats we doing here is called unit testing,meaning we are testing different units of the code.
#to do that we have imported our main python file as a module to this python file which specially made for testing the code of the main file

#normally we use simply if or try with print to quickly test parts of our code(like examples below)
#ex: 1.   if  square(x)==9:                          or   2.    try:
            # print(f"square of {x} is 9")                          assert square(3)==9
        # else                                                  except AssertionError:
            # print(f"square of {x} is not 9")                      print("square of 3 is not 9")
#- But there are 3rd party libraries made specifically to test your code more easily . pytest is one of them.you have to install it to use it (cmd --> pip install pytest) 
#pytest automatically add things if ,try,except,print so you have to type less lines of codes to test something 
#The assert keyword is used when debugging code.
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
#to pytest this you need to run this on cmd using this command:(cdm-->pytest UnitTesting.py) python only shows if there is bugs if not you will not see anything important on the output of the pytest
#according to SC50P lecture you dont need to call the functions at the bottom because pytest automatically call all the functions(but i don't know pytest is not working in this code if you don't call the functions)
from demo import *#demo is the main file we want to run tests on

def positive():#making function to test functions of the main file
    assert square(3)==9
    assert square(4)==16
    assert square(2)==7#intentionally made an error to see what pytest say
    assert square(6)==36
def negative():
    assert square(-8)==64
    assert square(-3)==-9#intentionally made an error to see what pytest say
    assert square(-2)==4
    assert square(-6)==-36#intentionally made an error to see what pytest say
def ZeroTest():
    assert square(0)==0

positive()
negative()# according to SC50P lecture They say there is no need to call the functions because pytest does it for you, but pytest doesn't run if i don't call the functions in this code.i dont know why(ask google) 
ZeroTest()