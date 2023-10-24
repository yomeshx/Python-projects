# label = an area widget that holds text and/or an image in a within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file ="photo.png")   #Creating a PhotoImage (importing a photo to use in a label)

                           #Creating a label  #Label(master , options )
label = Label(window,
                    text = "Damn ! Son..",      #text 
                    font = ("Arial",40,"bold"),
                    fg = "orange",
                    bg = "#161720",
                    relief = RAISED,    #border style -  RAISED /SUNK etc
                    bd = 10,
                    padx = 20,      #space between text and the border for x axis(above)
                    pady = 20,       #space between text and the border for x axis(below)
                    image = photo,
                    compound="bottom")  #when you deal with both text and images compound will give them a place    
label.pack()        #adding the label to the window ("margins and padding will be fitted to the text by default")
# label.place(x =100, y= 100) #another way  of adding the label but with exact pixel location of the window


window.mainloop()