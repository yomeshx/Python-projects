# daemon threads = a thread that runs in the background , not important for the program to run
#                   your program will not wait for daemon threads to compleat before exiting
#                   non-daemon threads cannot normally be killed, stay alive until task is complete 
#usage of daemon threads = background tasks,garbage collection, waiting for input, long running processes

import threading
import time

def timer ():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for ", count ," seconds")

thread_1 = threading.Thread(target=timer, daemon = True)
thread_1.start()

answer = input ("Do you wish to exit : ")

#-------------------------------------------------------------------
# you can convert non-daemon thread to a daemon thread or daemon thread to a non-demon by
# - using 'thread_name.setDaemon(True \ false)'
thread_1.setDaemon(True) #this should come before the  .start()

print(thread_1.isDaemon())  #isDaemon is to check if thread is daemon
