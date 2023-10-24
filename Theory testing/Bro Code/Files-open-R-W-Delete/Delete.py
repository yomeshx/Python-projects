import os

#1. Deleting a file or a empty directory
try:
    path = "D:\P\Programing\Python\My Learning Projects\Theory testing\Bro Code\Files-open-R-W-Delete\Coldplay.txt" #File path
    # path = "D:\P\Programing\Python\My Learning Projects\Theory testing\Bro Code\Files-open-R-W-Delete\\new"         #directory path
    if os.path.isfile(path):
        os.remove(path) #you cant delete a empty folder with this function only files
        print("File has been Deleted !")
    elif os.path.isdir(path):
        os.rmdir(path) #This will remove a empty directory
        print("Directory has been removed")
except FileNotFoundError:
    print("There is no such a File or Directory !")


#2. Removing(Deleting) a folder that is not empty
    #caution !!! this is very powerful
import shutil

shutil.rmtree("D:\M\Movies\How To Train Our Dragon (2018) [720p] [WEBRip] [YTS.MX]") #rmtree = remove tree