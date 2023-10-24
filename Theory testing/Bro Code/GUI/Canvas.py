# Canvas = widget that is used to draw graphs,plots,images, in a window

from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
canvas.create_line(0,0,500,500,fill="blue",width=5)#if you want you can assign to a variable "redLine = canvas.create_line()"
canvas.create_line(0,500,500,0,fill="red",width=5)
canvas.create_rectangle(50,50,250,250,fill="#00FF00")
canvas.create_polygon(250,0,500,500,0,500,fill="#F5D300",outline="#08F7FE",width=3) #1.normal method to give cordinents 

points = [500,0,500,500,0,250]
canvas.create_polygon(points,fill="#FE53BB",outline="black",width=3) #1.normal method to give cordinents 
canvas.pack()

window.mainloop()