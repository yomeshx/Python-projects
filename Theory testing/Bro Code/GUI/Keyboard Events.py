from tkinter import *

def dosomething(event):        # giving keyword event is necessary
    # print("You Pressed : " + event.keysym)
    label.config(text=event.keysym)
window = Tk()
# .bind() used for crete keyboard events 
            # "Return" stands for Enter button
window.bind("<Key>",dosomething) #we give event as the first argument and function in the second

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()

# event means a key press or other thing you do to trigger the function

#events ex:
    # "<Key>" - pressing any key triggers/calls the function
    # <"Return"> - pressing Enter triggers the function