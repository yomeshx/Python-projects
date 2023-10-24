#--------- Multi processing ----------

# multi processing = running tasks in parallel on different cpu cores , bypass GIL used for threading
        # multiprocessing = *better for CPU bound tasks (for tasks that require heavy cpu usage)
        # multi threading = *better for IO bound tasks (waiting around)


# in multiprocessing we are not limited to run only one thread at a time
# we run tasks parallel on different cpu cores
#Multiprocessing syntax are very similar to multi threading

from multiprocessing import Process,cpu_count
import time


def counter(num):
       count = 0
       while count < num :
            count += 1
def main() :                    #--->
        #------- One process --------
        # process_1 = Process (target = counter,args = (1000000000 , ))
        # process_1.start()
        # process_1.join()
        
        #------- Making divide the task in two processes --------
#instead of completing it in a single process we can make it in to two processes to make it faster

        print("CPU Core count : ",cpu_count()) #To check how many processors are there in your CPU

#my computer has only 4 cores , so more than 4 processes will slow down than speeding up
        process_1 = Process (target = counter,args = (250000000 , )) #if only one argument use ',' at the end.
        process_2 = Process (target = counter,args = (250000000 , ))
        process_3 = Process (target = counter,args = (250000000 , ))
        process_4 = Process (target = counter,args = (250000000 , ))
        process_1.start()
        process_2.start()
        process_3.start()
        process_4.start()

        process_1.join()    #Join - because Main process should wait till child process to be finished
        process_2.join()
        process_3.join()
        process_4.join()

        print("Finished in :",time.perf_counter()," seconds")

if __name__ == "__main__":      #if you running windows, you must add this' if __name__==__main__: main() and must write the code inside a function main
    main()
                                #If you did not add __name__== '__main__' protection
                                # -then you would enter a never ending loop of new process creation.
                                # -It goes like this:
                                #   -Your module is imported and executes code during the import 
                                #   -that cause multiprocessing to spawn 4 new processes.

                                #|<---