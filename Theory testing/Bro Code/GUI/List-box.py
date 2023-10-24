#a list box contains list of options you to choose
#you will see some previously learned GUI widgets are used here 
from tkinter import *

def submit():
    #print(lst_box.get(lst_box.curselection()))     #can be use for a case where only one item selection
    food = list()   #since we allows user to select multiple items
    for index in lst_box.curselection():    #for loop necessary to select multiple items in the listbox
        food.insert(index,lst_box.get(index))
    print("You have ordered :")
    for index in food :
        print(index)

def add_func ():
    lst_box.insert(lst_box.size(),entry_box.get()) #(index,item) #size function get you the next new index
     #we need to adages the window size whe we add new item
    lst_box.config(height = lst_box.size()) #size function will automatically make height of the window to fit the list

def del_func ():
    # lst_box.delete(lst_box.curselection())    #To delete a single item from the list
    #  #we need to adages the window size whe we delete an item
    for index in reversed(lst_box.curselection()): #Must reverse in order to delete all selected items
        lst_box.delete(index)

    lst_box.config(height= lst_box.size())


window = Tk()

lst_box = Listbox(window,
                    bg = "#f7ffde",
                    fg = "black",
                    font = ("Constantia",34,"bold"),
                    width = 12,
                    selectmode= MULTIPLE #allows you to select multiple items
                    )
lst_box.pack()

#   name.insert(index,"item")   #how to insert items in to the list box
lst_box.insert(1,"Pizza")
lst_box.insert(2,"Mac & Cheese")
lst_box.insert(3,"Soup")
lst_box.insert(4,"Salad")
lst_box.insert(5,"Garlic Bread")


entry_box = Entry(window,
                    font = ("Constantia",18,"italic")
                    )
entry_box.pack()

submit_btn = Button(window,
                    text = "|Submit|",
                    font = ("Arial",20),
                    command = submit
                    )
submit_btn.pack()

add_button = Button (window,
                        text = "Add",
                        font = ("Arial",20,"bold"),
                        command = add_func,
                        )
add_button.pack()

delete_button = Button (window,
                        text = "Delete",
                        font = ("Arial",20,"bold"),
                        command = del_func,
                        )
delete_button.pack()

 #config uses for making changes when need
lst_box.config(height = lst_box.size()) #size function will automatically make height of the window to fit the list

window.mainloop()