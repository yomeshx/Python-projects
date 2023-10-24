import re
import os

os.chdir("D:\P\Programing\Python\My Learning Projects\Theory testing\Regular Expressions")
f_handle = open("Coldplay.txt")

#******************* Wild Card Characters *******************#

# The dot character('.')matches any character
# Asterisk ('*') character is for 'zero or more'

for line in f_handle:
    line = line.rstrip()
    if re.search("^S.*:",line): #any line that's starts with 'S' and ends with ':' will mach the search
                                #'.'(any character) and '*'(zero or more) that is given between 'S' and ':' will make anything between suitable for the match .#
                                # even there's nothing between it will be a match, because '*' stands for zero or more
        print(line)