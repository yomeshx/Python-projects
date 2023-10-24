#normally we do
#------------------------
#ex:
File = open("D:\\C\\Orthodox.txt","a")
File.write("Hello World"+"\n")
File.close() #we need to close the file after using it

#The pythonic way
#------------------------
#if we use 'with' keyword then the open("D:...","w") function and assign it to a variable using 'as' keyword there is no need to close the file because it automatically closes the file after running indented lines
# ex
with open("D:\\C\\UnOrthodox.txt","a") as fileK:
    fileK.write("I am the king of pythonic"+"\n")