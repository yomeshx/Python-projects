from tkinter import *

#widgets = GUI elements : buttons ,textboxes, labels , images
# Windows = serves as a container to hold or contain these widgets

window = Tk()   #create a instance of a window

window.geometry("420x420")  # set the resolution of the window

window.title("yomesh_dk - First GUI")   #set the title of the window
    #importing and converting image to a PhotoImage to use it
icon = PhotoImage(file = "D:\P\Programing\Python\My Learning Projects\Theory testing\Bro Code\GUI\icon.png")   #importing the icon

window.iconphoto(True,icon)  #setting the icon to the window

window.config(background = "black")     #anytime when you want to make a change to the window

window.mainloop()   #to place window on computer screen and listen for events

#label.pack(anchor="center") giving a position to the widget