import shutil #There are several methods to copy a file,we use 'shutil' in this one

#shutil.copyfile() = copy contents of a file
# shutil.copy() = copy file() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (file's creation and modification times)


#1.****** shutil.copyfile() = copy contents of a file ******

#You need to give ,file you want to copy and name you gonna give to new copy file inside the shutil.copy() as arguments
# shutil.copyfile('filename or the file path with da file name' , name u want to give to your copy file or path you want to copy with da name u want to give to your copy file)
shutil.copyfile("D:\P\Programing\Python\My Learning Projects\Theory testing\Bro Code\Coldplay.txt","D:\P\Programing\Python\copy.txt")