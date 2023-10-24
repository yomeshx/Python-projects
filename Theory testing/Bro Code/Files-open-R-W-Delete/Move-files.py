import os #must import os

#source file and path
source = "D:\P\Programing\Python\My Learning Projects\Theory testing\Bro Code\Files-open-R-W-Delete\song.txt"
##this will move contents of the source file to a new path and new file you given bellow
#You can use same name or different name for the new file
destination = "D:\P\Programing\Python\My Learning Projects\Theory testing\Bro Code\move-test-txt.txt"

try:
    if os.path.exists(destination):
        print("File already Exists !")
    else:
        os.replace(source,destination)
        print("File has been moved !")
except FileNotFoundError:
    print("There is no such a file or a directory !")

#You can move a folder instead of a file 
    # EX: source = "D:\P\Programing\New folder"