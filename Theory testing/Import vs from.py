#A module is a collection of code or functions that uses the .py extension.
#A Python library is a set of related modules or packages bundled together.

#       There are several ways to import modules

#--- 1 ---
import time #This will import whole time module
#Down side - since we import the whole module we have to specify "moduleName.functionName()" all the time we use them
    # ex: time.sleep(5)
    # ex: winner = random.choice(["Alex","Brian"])
    # ex: number = random.randint(1,6)
#Up side - we don't need to worry about accidentally making a function with the same name.
#   ex: "lets say we define a function called 'sleep' it won't collide or overwrite sleep function in time module because we specify it as 'time.sleep()' all the time we use it."

#--- 2 ---
from tkinter import ttk #This will only import specific function or functions from the module,doesn't import whole module
#Up side - we dont need to say 'modulename.function' over and over we can just call it like a normal function (because it's in our namespace or in our scope)
    #ex:
        #from time import sleep
        #sleep(6)

        #from random import choice
        #name = choice(["John","Mia"])
# Down side - functions may collide (overwrite) if they have the same name
    #ex: let's assume we "from time import sleep" and also define a function called sleep. function we defined in our python file will overwrite the function we imported from the time module
        #from time import sleep
        #def sleep(no):     <-- this will overwrite the imported sleep
        #   for _ in range(no):
        #   print("I love Cod")