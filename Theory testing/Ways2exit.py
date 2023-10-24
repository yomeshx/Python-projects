import time

#There are many several ways to exit a program.the default way is ending the program. other ways are....

#--------------------------- Quit() --------------------------------

def qit ():
    ankara = input ("Type 'quit' to exit. : ")
    if ankara == "quit":
        print("Quitting...")
        time.sleep(2)
        quit()
    else:
        print(f"You entered {ankara}")

#---------------------------------Exit()------------------------------------------

def ext ():
    ankara = input ("Type 'exit' to exit. : ")
    if ankara == "exit":
        print("Exiting...")
        time.sleep(2)
        exit()
    else:
        print(f"You entered {ankara}")

#------------------------------------Sys.exit()-------------------------------------
# Sys module comes with a method called sys.exit() .it's another way to exit a program
import sys
def sysExt ():
    ankara = input ("Type 'syxit' to exit. : ")
    if ankara == "syxit":
        print("System Exiting...")
        time.sleep(2)
        sys.exit()
    else:
        print(f"You entered {ankara}")




# qit()
# ext()
sysExt()
