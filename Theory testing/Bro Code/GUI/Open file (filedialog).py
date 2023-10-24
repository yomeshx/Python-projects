from tkinter import *
from tkinter import filedialog

def selector ():
    file_path = filedialog.askopenfilename(initialdir="D:\\P\\Programing\\Python", #"initialdir" use to give a default path to open from.this is not neccesory to add
                                            title="Open your file",#title of the opening window
                                            filetypes=(("Text Files","*.txt"),("all kinds of files","*.*")) #you can limit what file types allowed to open
    
    )
    file = open(file_path,"r") #opening a file for reading purpose
    print(file.read()) # reading and printing the file
    file.close()    #it's wise to close a file after done with it

window = Tk()

buton = Button(window,
                        text = "click",
                        command= selector
)
buton.pack()

window.mainloop()