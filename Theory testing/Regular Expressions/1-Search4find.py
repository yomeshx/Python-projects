#Regular expressions are old style programming language itself.
#in order to use regular expression in python you should import a library called 're' .
#Regular expressions are very useful weapon to have in your arsenal.
#as soon as it find the result no code lines after that statement won't be executed !!!(So code bellow wont be run properly you have to comment out to test both method results)
#instead of using 'parameater.function()'(ex: line.find("Bla..blaa..") as we normaly do in python,
#- in regular expressions parameter comes inside the function after the thing you are looking for (ex: re.search("Hello",line))
#'re.search' will only return True or false value so it's great with something like if statements
import os
import re

os.chdir("D:\P\Programing\Python\My Learning Projects\Theory testing\Regular Expressions")
f_handle = open("Coldplay.txt")

###################### Using re.search instead of Find()#####################

#1. Finding some string with find function

# for line in f_handle:
#     line = line.rstrip()
#     if line.find("Hymn for the Weekend") >= 0 :
#         print(f"Using FIND function \n{line}")

# 2. Same thing but using regular expression re.search()
for line in f_handle:
    line = line.rstrip()
    if re.search("Songwriters",line):
        print(f"Using regular expression 're.search'\n{line}")

