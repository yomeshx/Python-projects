from tkinter import *
import os

os.chdir("D:\P\Programing\Python\My Learning Projects\Theory testing\Bro Code\GUI")
def submit ():
    print("The temperature is : " + str(scale.get()) +" degrees C")

window = Tk()

fire_image = PhotoImage (file ="button_img.png")
fire_Label = Label(image = fire_image)
fire_Label.pack()
scale = Scale(window,
                    from_ = 0,
                    to = 100,
                    length = 400,#size of the scale bar
                    orient = VERTICAL, #Orientation (HORIZONTAL or VERTICAL)
                    font = ("Consolas",15),
                    tickinterval= 10, #adds numeric indicators for value
                    bg = "black",
                    fg = "#FF1C00",#font color
                    # showvalue= 0,  #hide the current value when dragging the indicator down
                    troughcolor= "#69EAFF" ,#color of the bar,
                    )
# scale.set(50)   #set a Starting value on the scale bar by default
scale.set(((scale["from"]-scale["to"]) /2) + scale["to"])   #Starting value will be middle point of the scale bar by default
scale.pack()
button = Button(window,text = "Submit",command= submit)
button.pack()

window.mainloop()