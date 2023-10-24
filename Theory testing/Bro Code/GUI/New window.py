from tkinter import *

def create_window():
    # new_window = Toplevel() #Toplevel window depends on main window. if you close main one top level window also get closed
    new_window = Tk()   #Tk() makes a new window that independent. doesn't matter whether main one closed or not this one stays
    main_window.destroy() #if you want you can destroy a window. in this case this destroys the main one after new one created
main_window = Tk()


button = Button(text="Create New Window",
                font=("Ink free",20),
                bg="black",
                fg="white",
                activebackground="pink",
                command=create_window)
button.pack()

main_window.mainloop()