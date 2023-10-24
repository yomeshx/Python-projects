from tkinter import *

def submit ():
    user_name = entry.get() # get() will give us the input user gave
    print("Hello "+user_name)
    entry.config(state = DISABLED) #will disable the entry box to prevent from inserting

def del_ ():
    entry.delete(0,END) # "delete func takes positional args"

def back_ ():
    entry.delete(len(entry.get()) -1,END)

window = Tk()

entry = Entry(window,
                    font = ("Arial",50),
                    bg = "grey",
                    # show = "*" # if we want to show * when typing things like passwords
                        )
entry.insert(0,"Enter Name")    #displays a default value on the entry box


entry.pack(side = LEFT)

submit_button = Button(window,text ="Submit",bg = "white",fg = "black",command = submit)
submit_button.pack(side =RIGHT)

delete_button = Button(window,text = "Delete",font=("Arial",9,"bold"),bg = "black",fg = "white",command = del_)
delete_button.pack(side =RIGHT)

backspace_button = Button(window,text = "<- Backspace",font=("Arial",9,"bold"),bg = "#161720",fg = "white",command = back_)
backspace_button.pack(side =RIGHT)

window.mainloop()