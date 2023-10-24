import os           #must import os module

path_r = "D:\P\Programing\Python\My Learning Projects\Theory testing\Bro Code" #path as a variable
#sometimes you have to use 2 '\\' to skip backslashes

#Checking if the path exists and the file exists 
if os.path.exists(path_r):      #Checking if the path exists
    print("Location Exists !")
    if os.path.isfile(path_r):  #to check if the path is a file
        print ("Path is a file !!!")
    elif os.path.isdir(path_r):
        print("path is a directory !!!")

else:
    print("Location doesn't Exists !")
