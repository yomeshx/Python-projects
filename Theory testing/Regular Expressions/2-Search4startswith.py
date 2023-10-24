#you can use ^ symbol inside "" and before the string when using re.search, this does same thing startswith does..

import os
import re

os.chdir("D:\P\Programing\Python\My Learning Projects\Theory testing\Regular Expressions")
f_handle = open("Coldplay.txt")

###################### Using re.search instead of startswith()#####################


# Using startswith function

# for line in f_handle:
#     line = line.rstrip()
#     if line.startswith("Life"):
#         print(line)

# Using re.search("^word",line)

for line in f_handle:
    line = line.rstrip()
    if re.search("^Life",line):
        print(line)