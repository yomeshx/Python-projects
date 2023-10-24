from tkinter import *

def open_file():
    print("file opened")
def save_file():
    print("file saved")
def exit_file():
    print("file exited")
#------------Edit menu-------------
def paste_file():
    pass
def copy_file():
    pass
def cut_file():
    pass
window = Tk()

#-----------Importing photo icons--------------
newImage = PhotoImage(file="D:\\P\\Programing\\Python\\My Learning Projects\\Theory testing\\Bro Code\\GUI\\Icons\\button_img.png")
openImage = PhotoImage(file="D:\\P\\Programing\\Python\\My Learning Projects\\Theory testing\\Bro Code\\GUI\\Icons\\location.png")
saveImage = PhotoImage(file="D:\\P\\Programing\\Python\\My Learning Projects\\Theory testing\\Bro Code\\GUI\\Icons\\music.png")

menubar = Menu(window)
window.config(menu=menubar) #You should specify that you are using a menu on your window

fileMenu = Menu(menubar,tearoff=0,font = ("MV Boli",15),bg="#00FF00") #you should add sub menu to the main menu just like adding widget to a window 
                                    #tear off remove the broken line in the dropdown menu

menubar.add_cascade(label="File",menu=fileMenu) #you should give a label to every submenu and it's options. AkA - 'commands'

fileMenu.add_command(label="Open",command=open_file,image=newImage,compound="left")    #add_command add an option to the dropdown menu #command is for to give a function 
fileMenu.add_command(label="Save",command=save_file,image=openImage,compound="left")
fileMenu.add_separator() # A line to separate
fileMenu.add_command(label="Exit",command=quit,image=saveImage,compound="left") # To exit a window you can just use built in quit function
#------------------------------------------------------------

edit_menu = Menu(menubar,tearoff=0,font = ("MV Boli",15))

menubar.add_cascade(menu=edit_menu,label="Edit")

edit_menu.add_command(label="Paste",command=paste_file)
edit_menu.add_separator()
edit_menu.add_command(label="Copy",command=copy_file)
edit_menu.add_command(label="Cut",command=cut_file)

window.mainloop()