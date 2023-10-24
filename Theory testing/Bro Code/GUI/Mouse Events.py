from tkinter import *

def dosomething(event):
    print("He Clicked It !")
    print("Mouse Coordinates: "+"X= "+ str(event.x)+" Y= "+str(event.y)) #shows the mouse position when clicked

window = Tk()


# window.bind("<Button-1>",dosomething)# <Button-1> = Left Mouse Button

# window.bind("<Button-2>",dosomething)# <Button-2> = Middle Mouse Button\aka Scroll wheel

# window.bind("<Button-3>",dosomething)# <Button-3> = Right Mouse Button

# window.bind("<ButtonRelease>",dosomething)# <ButtonRelease> = When you release a mouse button

# window.bind("<Enter>",dosomething)# <Enter> =Not the Enter key.
                                #  This will look at exact coordinates your cursor entered the window

# window.bind("<Leave>",dosomething)# #  This will look at exact coordinates your cursor leave the window

window.bind("<Motion>",dosomething)# #  Constantly tracking mouse position . Helpful to use in games

window.mainloop()