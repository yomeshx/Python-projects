from tkinter import *

root = Tk()
root.geometry("420x420")
root.title("root-melons")
root.config(background = "grey")

count = 0
def click_action ():
    global count        # "global" before the variable to use a variable outside the function you should use
    count += 1
    print(f"Clicked {count} times")

#button_img = PhotoImage(file = "button_img.png")
button = Button(root,
                    text = "Click ME",
                    font = ("Arial",10,"bold"),
                    bg = "#00ff00",
                    fg = "black",
                    bd = 3,
                    activebackground="grey",
                    activeforeground="blue",
                    command = click_action,
                    state = ACTIVE ,
                    #image = button_img,
                    compound= "bottom"
                    )
button.pack()

root.mainloop()
