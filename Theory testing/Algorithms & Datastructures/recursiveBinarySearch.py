#There is actually more than one way to write a binary search algorithm.we wrote first version of writing in "binarySearch.py". and this version called "Recursive Binary Search"
#Recursive Binary Search is very confusing and easily forgettable theory, look at 01:34:55 video below
    #--> D:\P\Programing\Algorithms and Data Structures\Basics\Algorithms and Data Structures Tutorial - Full Course for Beginners(720P_HD).mp4
#instead of using while loop, recursive functions call itself until they met the expected target.
#Note: inside a recursive binary search includes a return statement

def recursiveBinarySearch(list,target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursiveBinarySearch(list[midpoint+1:],target)  #instead of while loop in RecursiveBinarySearch we call the function again with splitted versions of the list
            else:
                return recursiveBinarySearch(list[:midpoint-1],target)

def verify(result):
    print(f"Target found : {result}")

numbers = [1,2,3,4,5,6,7,8]


result = recursiveBinarySearch(numbers,12)
verify(result)
result = recursiveBinarySearch(numbers,8)
verify(result)