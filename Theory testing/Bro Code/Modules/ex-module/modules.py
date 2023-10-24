#There are two ways to import modules 

# 1. <----- import -----> To import a module (with all the functions and classes etc)
import os as msg

# 2. <----- from -----> To import only specific functions from the module

from os import chdir,path       #importing specific things from the module
from os import *       #importing everything in the module works same as "import os" but not recommended cause can run in to errors

#when you use from to import modules you dont have to use module name before the function 
    # ex :  import            from
    #       os.chdir()      chdir()