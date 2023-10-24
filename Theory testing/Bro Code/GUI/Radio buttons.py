#Radio buttons similar to check box but you can only select one from a group

from tkinter import *

food = ["Pizza","Hamburger","Hot Dog"]

def run_dis ():
    if (x.get()) == 0 :
        print("Your Pizza will be ready in few minutes")
    elif (x.get()) == 1 :
        print("Your Hamburger will be ready in few minutes")
    elif (x.get()) == 2 :
        print("Your Hot Dog will be ready in few minutes")
    else:
        print("Huh ?")
window = Tk()

location = PhotoImage(file = "location.png")
music = PhotoImage(file = "music.png")
video = PhotoImage(file = "video.png")

images_lst = [location,music,video] 

x= IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                                text = food[index], #add text to radio buttons
                                variable = x, #group radio buttons together if they share same variable
                                value = index, #assigns each radio button a different value
                                padx = 25, #adds padding on x axis
                                font = ("Impact",25),   #font style and size
                                image = images_lst[index], #get images to each radio button
                                compound = "left",
                                indicatoron = 0, #this will eliminate indicator shown inside the button by default
                                width = 375,
                                bg = "#00FF00",
                                activeforeground= "yellow",
                                activebackground="black",
                                command= run_dis
                                )
    radiobutton.pack(anchor = W) #or you can use "w" , this align the radio button to the west

window.mainloop() 