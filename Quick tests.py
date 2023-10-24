from tkinter import *
from tkinter.ttk import *
from time import strftime

def time  ():
    string = strftime("%H:%M:%S %p")
    label.config(text = string)
    label.after(1000,time)
root = Tk()
root.title("Clock app")
label = Label(root,font=("Consolas",50,"bold"),background="black",foreground="cyan")
label.pack(anchor="center")
time()
root.mainloop()