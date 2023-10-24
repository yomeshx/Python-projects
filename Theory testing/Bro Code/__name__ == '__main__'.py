#Modules refer to a file containing Python statements and definitions. 
# A file containing Python code, for example: example.py , is called a module, and its module name would be example .

#There are two ways modules(python file) can be run
    # *1. Modules can be run as stand alone program 
    # *2. or Modules can be imported and used by other modules 

#if __name__ == "__main__": 
# is the way to identify if it's the main module that run directly or a imported one
#this function allows our modules to have some flexibility 
#python interpreter sets "special variables" one of which is __name__ is assigned as main if it runs directly 
#when you import a python file to a another python file as method ,it reads the whole imported file.so there is a chance if there are function calls or other stuff to accidentally get executed.and this __name__=='__main__' prevents you accidentally doing that because it recognize that file whether a imported one or not(means directly running)

#--------------------------------------------------------------------------------------
if __name__ == "__main__":              #Checking if this module is the main one
    print("This Module Runs Directly")
else:
    print("This Module Is an Imported Module And Runs Indirectly")
#--------------------------------------------------------------------------------------
import os
if os.__name__ == "__main__":           #Trying same thing but on a imported module
    print("This Module Runs Directly")
else:
    print("This Module Is an Imported Module And Runs Indirectly")
#--------------------------------------------------------------------------------------