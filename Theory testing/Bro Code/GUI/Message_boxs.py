from tkinter import *
from tkinter import messagebox      #should import messagebox as a submodule

def w_r_n ():
#---------------------------------------------------------------------------------------------------------------------
    messagebox.showinfo(title="INFO",message="Done!")   #To show an regular message (info)
    messagebox.showwarning(title="WARNING!",message="You almost died !")    #To give a warning message
    messagebox.showerror(title="Error Unknown!",message="Something went wrong!!!")  #to show an error message
#---------------------------------------------------------------------------------------------------------------------
                #things under the "if" line will run if the thing become true (meaning "ok or yes" button pressed) 
    #----------------------#AskOkcancel--------------------------
    if messagebox.askokcancel(title="OK or Cancel",message="Do you want to arrange a meeting ?"): #AskOkcancel
        print("Arrange a meeting")
    else:
        print("Meeting cancelled!")
    #---------------------#Askretrycancel---------------------------
    if messagebox.askretrycancel(title="Retry or Cancel",message="Do you want to try again ?"): #Askretrycancel
        print("He wants to try again")
    else:
        print("He don't want to try again!")
    #---------------------#Askyesno---------------------------
    if messagebox.askyesno(title="Yes Or No",message="Do you love me ?"):   #AskYesno
        print("She loves me")
    else:
        print("She doesn't love me")

    #---------------------#AskQuestion---------------------------
        #unlike others this doesn't return a boolean value as True or False this returns a answer.so you can assign it to a variable
    answer = messagebox.askquestion(title="Ask question",message="Do you like to eat kottu ?")
    if (answer == "yes"):
        print("Answer is yes")
    else:
        print("Answer is no")

    #---------------------#Askyesnocancel---------------------------
        # This returns True = yes , False = no , None = cancel
    askit = messagebox.askyesnocancel(title="YesNoCancel",message="Do you know about Ukraine war ?",icon="error")
    if (askit == True):
        print("He knows about the war")
    elif (askit == False):
        print("He doesn't know about the war")
    elif (askit == None):
        print("He avoided the question")
    else:
        print("invalid answer")

#You can also use a icon for the message box as you desired
    # if messagebox.askyesno(title="YesNo",message="Give an answer!", icon= "info"):
    #     pass
    # if messagebox.askyesno(title="YesNo",message="Give an answer!", icon= "error"):
    #     pass
    # if messagebox.askyesno(title="YesNo",message="Give an answer!", icon= "warning"):
    #     pass
#---------------------------------------------------------------------------------------------------------------------


window = Tk()

wrnbtn = Button (window,
                        text = "W.R.N",
                        fg = "red",
                        command=w_r_n
)
wrnbtn.pack()
window.mainloop()