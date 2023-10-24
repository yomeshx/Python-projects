from tkinter import *
from tkinter import colorchooser


def piccol():
    color = colorchooser.askcolor()
    print(color)    #testing what askcolor returns
    rem = color[1]  #because askcolor returns a tuple with 0 position is rgb values and 1 position is hex value.we need the hex
    window.config(background=rem) #Changing the background

def piccolbtn():
    color = colorchooser.askcolor()
    print(color)
    rem = color[1]
    btn2.config(bg=rem)
window = Tk()
window.geometry("480x480")
btn = Button(window,text="Background_color",command=piccol)
btn.pack()
btn2 = Button(window,text="Button_color",command=piccolbtn)
btn2.pack()

window.mainloop()