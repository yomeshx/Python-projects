#Frame is a rectangular container to group and hold widgets

from tkinter import *

window = Tk()
window.geometry("420x420")
frame = Frame(window,bg = "pink",bd = 5,relief=SUNKEN)
frame.pack(side=BOTTOM) #side is for specify which side this widget stick to in the window.in this case it's the bottom
# frame.place(x=0,y=0) #you can use place(x,y cordinants) instead of using pack() + side #in this case it will stick to top left corner 

Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP) #if you dont want a name you can just not assign it to a variable(mostly for testing purposes)
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT) #if you dont want a name you can just not assign it to a variable(mostly for testing purposes)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT) #if you dont want a name you can just not assign it to a variable(mostly for testing purposes)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT) #if you dont want a name you can just not assign it to a variable(mostly for testing purposes)
window.mainloop()