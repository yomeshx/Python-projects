def linear_search(list,target):#this function returns index position of the target if found, else returns None
    for i in range(0,len(list)):#this iterates index positions not items in the list
        if list[i] == target:
            return i
    return None

#------------------ Testing the function above ---------------------
def testing(index): #to test the above linear_search function
    if index is not None:
        print("Target found at index : ",index)
    else:
        print("Target not found !")

numbers = [1,2,3,4,5,6,7,8,9,10]#the list

indexx = linear_search(numbers,6)#calling function and storing it in a variable
testing(indexx)#testing
indexx = linear_search(numbers,8)
testing(indexx)