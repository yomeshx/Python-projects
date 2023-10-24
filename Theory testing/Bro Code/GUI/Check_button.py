from tkinter import *

def display ():
    if (x.get()==1):
        print("You agree!")
    else:
        print("You don't agree!")
window = Tk()

x = IntVar() #Integer variable to store the value that takes from the checkbox input.
            # (if its a bool "BooleanVar" )
            # (if its a string "StringVar" )
window.config(background ="black")

window.title("Check-Button (check-box)")
music_icon = PhotoImage(file="music.png")
check_box_agree = Checkbutton(window,
                                text = ("Agree with terms"),
                                variable= x,#variable to store value of the checkbox 1 or 0 (on / off)
                                onvalue = 1,#if box is checked VALUE will be 1 (you can assign boolean or other value tooo)
                                offvalue=0, #if box is checked VALUE will be 0
                                command = display,
                                font=("Arial",20),
                                fg = "#00FF00",
                                bg = "black",
                                activeforeground= "red",
                                activebackground= "#161720",
                                padx = 25,
                                pady = 10,
                                image =music_icon,
                                compound = "left")
check_box_agree.pack()

window.mainloop()