from tkinter import *

def show_txt ():
    txt_input = text_area.get(1.0,END) # 1.0 stand for starting point(beginning) of the text are and END is the end point
    print(txt_input)

window = Tk()

text_area = Text(window,
                        font=("Ink Free",24), #when you change the font size you also change the window size
                        height=8,      #therefore you also need to set width and height to limit expansion of the window size  
                        width= 20,
                        padx=20, # because of the padding text wont be sticking to a side
                        pady=20,
                        bg = "light yellow",
                        fg = "purple"
                        )
text_area.pack()
button = Button(window,
                        text="Click",
                        command= show_txt
)
button.pack()
window.mainloop()