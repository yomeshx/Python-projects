from tkinter import*
from tkinter import ttk 
import time


def down_f():
    GB =100    #total file size ,means progress bar has 100 checkpoints to reach to the end (100%/100) =1%
    download =0     #current amount of downloaded GB
    speed = 1
    while (download<GB):
        time.sleep(0.02)
        bar["value"]+=(speed/GB)*100    #because progress bar divided to 100 points means 1%x100 =100% 
        download+=speed    #downloaded GB + speed
        percent.set(str(int((download/GB)*100))+"%") #setting or updating variable label value
        text.set(str(download)+"/"+str(GB)+" GB downloaded") #no of downloaded GBs / total size
        window.update_idletasks() #after each iteration window gonna update\refresh.so we see the progress of the progress bar in each iteration
                                #if you don't use this you will wait until loop complete and show the end result.which is not what we want
window = Tk()

percent = StringVar() #percentage defined as a string variable to be used in the variable label
text = StringVar() #percentage defined as a string variable to be used in the variable label

bar = ttk.Progressbar(window,orient=HORIZONTAL,length=300)  #ttk method has the Progressbar . Orient HORIZONTAL\"horizontal" or VERTICAL\"vertical"
bar.pack(pady=10)#if you pack this bar in one line there will be a error .so pack like this

percentLabel = Label(window,textvariable=percent).pack() #text variable allows you to make a text variable label
taskLabel = Label(window,textvariable=text).pack() #text variable allows you to make a text variable label

button= Button(window,text="Download",fg="white",bg="black",command=down_f).pack()

window.mainloop()