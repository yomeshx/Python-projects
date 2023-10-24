from tkinter import *
from tkinter import ttk #ttk imports special module that we need in order to create notebooks

window = Tk()

notebook = ttk.Notebook(window) #Widget that manages a collection of window/displays

tab1= Frame(notebook) #new frame for tab 1  #Frames group multiple widgets in to a one unit
tab2= Frame(notebook) #new frame for tab 2s

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack(expand=True,fill="both") #Expand to fill any space not otherwise used
                            #'fill =' will fill space on x or y axis as given .
                            # -you can use option "both" instead of x or y to fill space from both sides

                    #now you can add contents to your tabs
Label(tab1,text="Hello, this is a tab No.01",width = 50,height=25).pack() # label of the tab change width and height of the tab
Label(tab2,text="Hello, this is a tab No.02",width = 50,height=25).pack()

window.mainloop()

#a tab means a frame.because it is a unit of many things grouped together
#So notebook is a big container you can put all your tabs that are in the form of frames.
# just like in menu bars we add sub menus to the main menu you add tabs("aka frames") to the notebook 