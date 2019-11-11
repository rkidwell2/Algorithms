
"""
Max heap file.
Max heap property: Each node is less than or equal to parent node 
Stored as a list of objects, no nodes needed
"""

def getParent(index):
    if index == 0:
        return None
    return (index-1)/2
    
def leftChild(heap, index):
    return index*2 + 1 

def rightChild(heap, index):
    return index*2 + 2 
    
def maxheapify(myArr, size, index):
    #index is index of subtree's root
    val = myArr[index] #store index value to use as reference
    
    leftI = leftChild(myArr, index)
    rightI = rightChild(myArr, index) #if returns none, no child exists
    
    maxIndex = index #put max as index, then see if needs to be changed
    
    if leftI < size and val < myArr[leftI]:
        #print("comparing ", val, "and ", myArr[leftI])
        maxIndex = leftI
        
    if rightI < size and myArr[maxIndex] < myArr[rightI]:
        
        maxIndex = rightI
        
    if maxIndex!=index:
        myArr[index], myArr[maxIndex] = myArr[maxIndex], myArr[index]
        #print("swapped ", myArr[index], "and", myArr[maxIndex])
        maxheapify(myArr, size, maxIndex)
        
def buildMaxHeap(myArr):
    #Find index of last non-leaf node
    n = int(len(myArr)/2 -1)
    for i in range (n, -1, -1):
        maxheapify(myArr, len(myArr), i)
    return myArr
        
def heapSort(myArr):
    #first build the max heap
    myArr = buildMaxHeap(myArr)
    
    #go through each element, swapping first and last
    for i in range(len(myArr) -1, 0, -1):
        myArr[0], myArr[i] = myArr[i], myArr[0]
        maxheapify(myArr, i, 0)
        
    return myArr
 
mynums = [6, 4, 10, 2, 0, 98, 34, 60, 75, 3, 91, 11, 7]

#buildMaxHeap(mynums)
#print("Max heap is: ", mynums)


#heapSort(mynums)
#print("After heap sort: ", mynums)