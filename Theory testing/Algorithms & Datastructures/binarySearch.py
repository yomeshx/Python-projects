##There is actually more than one way to write a binary search algorithm.this is one way to do it(here we use while loop)
def binarySearch (list,target):
    first = 0               #because 1st index of a list is 0
    last = len(list) -1     #because 1st index of a list is 0
    count =0
    while first <= last:    #because list split into half each time until it become a single value
        midpoint = (first+last) //2
        count+= 1   #for testing purposes
        if list[midpoint] == target:
            return midpoint,count
        elif list[midpoint] < target:
            first = midpoint +1
        elif midpoint > target:
            last = midpoint -1
    return None,count #if the target not in the list

#------------------ Testing the function above ---------------------
def testing(index,rounds): #to test the above linear_search function
    if index is not None:
        print(f"Target found at index : {index},Rounds of splits :{rounds}")
    else:
        print("Target not found !")


li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#the test list above is already in order.so we assume there is no need to run a sorting algorithm first before using in binary search 
#if the values in the are unsorted our implementation of binary search may return "None" even the value existed in the list
TargetIndex,rounds =binarySearch(li,10)#test 1 - should find expected target first round
testing(TargetIndex,rounds)

TargetIndex,rounds =binarySearch(li,20)#test 2
testing(TargetIndex,rounds)

TargetIndex,rounds =binarySearch(li,15)#test 3
testing(TargetIndex,rounds)

TargetIndex,rounds =binarySearch(li,60)#test 4 - There is no value as 60 in the list so "Target not found!"
testing(TargetIndex,rounds)