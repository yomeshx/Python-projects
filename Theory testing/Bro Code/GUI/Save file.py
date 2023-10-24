from tkinter import *
from tkinter import filedialog

def btn ():
    file = filedialog.asksaveasfile(title="Save this file ?",
                                    initialdir="D:\\",
                                    defaultextension=".txt",
                                    filetypes=([
                                        ("Text File","*.txt"),
                                        ("Html","*.html"),
                                        ("All files","*.*")
                                                ])
                                        )
    if file is None:    #if you click save but then decided to close the window without saving it shows an error.to avoid that we can use this
        return
    
    # clipboard = input("Write here :\n")   #You also can Get the input from Terminal #press save and make a file then terminal wil ask for the input
    clipboard = str(text.get(1.0,END))    #Get the input from GUI text area
    file.write(clipboard)
    file.close()
window = Tk()
window.title("Save text")
window.geometry("240x240")
button = Button (window,
                        text="Save",
                        command=btn)
button.pack()
text = Text(window,
                    font=("Ink Free",24),
                    bg = "light yellow"
                    )
text.pack()
window.mainloop()