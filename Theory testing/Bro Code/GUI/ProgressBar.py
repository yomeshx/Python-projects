from tkinter import *
from tkinter import ttk
import time
def proGress():
    tasks = 5
    completed=0
    while (completed<tasks):
        time.sleep(0.6)
        completed+=1
        percent = (completed/tasks)*100
        proBar["value"]+=(1/tasks)*100
        task_count.set(str(completed)+"/"+str(tasks))
        percentageDis.set(str(int(percent))+"%"+" Downloaded")
        window.update_idletasks()
window = Tk()

task_count = StringVar()
percentageDis = StringVar()

proBar = ttk.Progressbar(window,orient=HORIZONTAL,length=400)
proBar.pack(pady=20)

button = Button(window,text="Start",command=proGress).pack()
taskLabel = Label(window,textvariable=task_count).pack()
percentLabel = Label(window,textvariable=percentageDis).pack()

window.mainloop()