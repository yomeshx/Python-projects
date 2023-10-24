
with open("D:\P\Programing\Python\My Learning Projects\Theory testing\Bro Code\Coldplay.txt") as file:
    print(file.read())

#open files with "with" will automatically close the file after using them
#to test that,
print(file.closed) #will print "True" because file is closed