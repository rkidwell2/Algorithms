"""
Sorter file with heapsort, mergesort, and quicksort
"""

from MaxHeap import heapSort
from random import randint

def mergesort(myArr):
    n = len(myArr)
    #Split up arrays into subarrays with recursive calls
    if n > 1:
        half = n//2
        left = myArr[:half]
        right =myArr[half:]
        
        mergesort(left)
        mergesort(right)
        
    #actual merge functionality here    
        #initialize counters
        x = 0 #Keep track of left arr position
        y = 0 #Keep track of right arr position
        z = 0 #Keep track of myArr position
    
        lLeft = len(left)
        rRight = len(right)
        
        while x < lLeft and y < rRight:
            #Go through subarrays adding 
            if left[x] <= right[y]: 
                myArr[z] = left[x]
                x += 1 #Move pointer of left over
            elif left[x] > right[y]:
                myArr[z] = right[y]
                y +=1 #Move right pointer over
            z += 1
            
        while x < lLeft:
            myArr[z] = left[x]
            x += 1
            z += 1
        
        while y < rRight:
            myArr[z] = right[y]
            y += 1
            z += 1   
            


def quicksort(arr):
    #Use this helper function so we can just call quicksort with only the array
    n = len(arr) -1 
    quicksortRecurse(arr, 0, n)

def quicksortRecurse(array, lowest, highest):
    if lowest < highest:
        #find pivot at partitioning index
        piv = findPartition(array, lowest, highest)
        
        #sort each half
        quicksortRecurse(array, lowest, piv -1)
        quicksortRecurse(array, piv+1, highest)
    
def findPartition(array, lowest, highest):
    pivot = array[highest]
    i = lowest-1
    
    
    for x in range(lowest, highest):
        if array[x] <= pivot:
            i += 1
            array[i], array[x] = array[x], array[i]
    array[i+1], array[highest] = array[highest], array[i+1]
    return i+1
    
    
def buildArray(x):
    """
    Function to build an unsorted array of random integers
    of size x
    used for testing purposes
    """
    array = []
    for x in range (0,x):
        array.append(randint(-1000, 2000))
    return array

