from tkinter import *


root = Tk()
root.geometry("480x480")
root.title("This is a test!")
root.config(background="grey")
def hello():
    print("Hello")

button = Button(root,
                    bg= "blue",
                    fg= "white",
                    text = "Hello",
                    bd = 3,
                    activeforeground = "red",
                    activebackground= "black",
                    command = hello,
                    state= ACTIVE,
                    compound="bottom"
)
button.pack()
root.mainloop()
