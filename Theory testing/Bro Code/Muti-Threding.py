#Thread = a flow of control
#multiple threads can be in charge of executing different parts of the program almost feel like multiple threads running at once(but their not.each thread takes a turn) 
# GIL = (Global interpreter lock ) allows only one thread to hold the control of the python interpreter
#There are two kinds of catagories of programs/Tasks based on time they spend 
    # 1.CPU bound = Tasks\programs that spends most of it's time waiting for internal events (CPU intensive)
                    #** Multiprocessing - true parallel execution of multiple processes using more than one processor
    # 2.Io bound  = Tasks\programs that spends most of it's time waiting for external events (User inputs,Web scraping)
                    #** Multithreading - All threads takes turns to run concurrently but almost feel like multiprocessing



#--------------------------------------------------------------------------------------------------
# Ex 1 :
import time,threading

def eat ():
    time.sleep(3)
    print(f"Done Eating")
def code ():
    time.sleep(2)
    print("Done Coding")
def sleep():
    time.sleep(3)
    print("Done Sleeping")

# eat()
# code()        Testing- Normally this processes takes 6 second to complete,but threading will decrease the time
# sleep()

thread_1eat = threading.Thread(target = eat, args = ())
thread_1eat.start()

thread_2code = threading.Thread(target = code,args = ())
thread_2code.start()

thread_3sleep = threading.Thread(target =sleep ,args = ())
thread_3sleep.start()


print("Thread Count : ",threading.active_count()) #to get the count of active threads
print("Thread List : ",threading.enumerate())    #To get list of all the threads that are running
print(time.perf_counter())    #performance counter gives how many time it take our main thread to complete its job

# you may noticed that last three print lines in the code executed first in the program because
#-they are contents of the main thread and main thread is not in charge of executing codes belongs to other threads 
#-so it don't wait around to others to finish and runs first

#in this program main threads job is to order constructions to create 3 more threads and execute thing outside and those 3 new threads(which means things belongs to main thread)
#---------------------------------------------------------------------------------------------------





#---------- Thread synchronization -----------

#main thread finish first ,but if we want to main thread to wait till other threads to complete before main one, 
#-thread synchronization is the way to do that
#  We use " 'thread_name'.join() " method to do that


# ex:2                  #same code above used in this example
print("\n-----------------------------------------------------------\n")
import time,threading

def eat ():
    time.sleep(3)
    print(f"Done Eating")
def code ():
    time.sleep(2)
    print("Done Coding")
def sleep():
    time.sleep(3)
    print("Done Sleeping")


thread_1eat = threading.Thread(target = eat, args = ())
thread_1eat.start()

thread_2code = threading.Thread(target = code,args = ())
thread_2code.start()

thread_3sleep = threading.Thread(target =sleep ,args = ())
thread_3sleep.start()

#****************************
thread_1eat.join()
thread_2code.join()             #because of we use join to synchronize other threads main will execute last
thread_3sleep.join()            #(#because Main thread should wait till child threads to be finished)
#****************************

print("Thread Count : ",threading.active_count()) #to get the count of active threads
print("Thread List : ",threading.enumerate())    #To get list of all the threads that are running
print(time.perf_counter())    #performance counter gives how many time it take our main thread to complete its job
