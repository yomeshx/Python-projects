from tkinter import *
from tkinter.ttk import *
from time import strftime

def time():
    string = strftime("%H:%M:%S %p")#separator can be anything you put in between ex# ':' ',' '.' '\' '/' '|' ......
    label.config(text=string)
    label.after(1000,time)   #after method calls a function once after given time... '.after(time in milliseconds ,function to be called without brackets)'

root = Tk()
root.title("Clock app")
label = Label(root,font=("Consolas",40,"bold"),background="#161720",foreground = "#ADD8E6")
label.pack(anchor="center")
time()
root.mainloop()