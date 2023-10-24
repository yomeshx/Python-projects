# .grid() is used for positioning the widget in your window.
#.pack() and .place() is also methods to position a widget in a window
# but grid allows you to position a widget like in a excel sheet .
# it's a table like structure
# you have columns and rows that has a number
# so you can place widget inside those cells like this ex: text.grid() 
#and the width of a column depends on largest widget contained in that column ex : first name
#                                                                               #  address to your home <--this will be the width of the column 
                                                                                #  last name
                                                                                #  pet name
                                                                            #but you can change this default width by giving "width="
                                                                               #ex: Label(window,text="Bla Bla", width = 10) 
from tkinter import *


window = Tk()
window.title("Grid Example")

titleLabel = Label(window,text="♦-♣| Enter Your Info |♣-♦",font=("Arial",22),bg="grey",fg="#00FF00").grid(row=0,column=0,columnspan=2)

firstNameL = Label(window,text="First Name : ",font=("Arial",19),bg="grey").grid(row=1,column=0)
firstNameEntry = Entry(window,font=("Arial",19),bg="black",fg="white").grid(row =1,column =1)


lastNameL = Label(window,text="Last Name : ",font=("Arial",19),bg="grey").grid(row=2,column=0)
lastNameEntry = Entry(window,font=("Arial",19),bg="black",fg="white").grid(row =2,column =1)


emailL = Label(window,text="Email : ",font=("Arial",19),bg="grey").grid(row=3,column=0)
emailEntry = Entry(window,font=("Arial",19),bg="black",fg="white").grid(row =3,column =1)

submit_button=Button(window,text="Submit",font=("Ink free",13),activebackground="purple",activeforeground="white").grid(row=4,column=0,columnspan=2)

window.config(background="grey")
window.mainloop()