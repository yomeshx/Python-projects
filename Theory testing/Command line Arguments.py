# We can give arguments to the command line before running it
    #ex:'sys' module. read for more: https://docs.python.org/3/library/sys.html

#example:
import sys

print("Hello, my name is", sys.argv[1])# we should type in the terminal-->  python filename.py yomesh 
#argv is like a magical list variable.
#it stores arguments we enter into a list.
#so we can use indexing to use them.
#but 0 index A.k.a 'sys.argv[0]' always store the name of the python file.
#-so our arguments starts from index 1,.... 

#---------------------------------------------------------------------------------------

# if you don't give an argument to the command line, there will be no argv[1],so there will be an error
#-to bypass this we can use 1.try-except or 2.if conditions

# --1.try-except solution--
import sys
if len(sys.argv) < 2:
    print("Please give an argument")#ex : python name.py
elif len(sys.argv) > 2:
    print("Too much arguments")# ex : python name.py yomesh dissanayaka   #because space is the separator when giving multiple arguments
    #-therefore yomesh[space]dissanayaka counts as 2 arguments.
    #-you can avoid that by using quotations ex: "yomesh dissanayaka" (this will be recognized as a one argument)
else:#means exactly two items in the argv list argv[0] is the file name argv[1] is the argument we gave
    print("Hi my name is", sys.argv[1])#ex : python name.py yomesh

#--2.if conditions solution--
import sys
try:
    print("Hi my name is",sys.argv[1])
except IndexError:
    print("No Command Line Argument is given!")



#------------------------------------------------------------------------
#skipping first item aka name of the programme and printing all the other items in the list
import sys

if len(sys.argv) < 2:
    sys.exit("No argument given")
for arg in sys.argv[1:]:
    print("Hello my name is" ,arg)