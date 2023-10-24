import re,os
os.chdir("D:\P\Programing\Python\My Learning Projects\Theory testing\Regular Expressions")

f_handle = open("Coldplay.txt")
for line in f_handle:
    line = line.rstrip()
    if re.search("^Wh\S+n",line): # '\S' = Non white space characters
                                    #'+' = one or more
        print(line)                 #so this code means that words that starts with 'Wh' and ends with 'n' and exist one or more non whitespaces between these
                                    #-two will be a match 