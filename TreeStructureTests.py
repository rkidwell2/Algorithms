from AVLTree import *
from BSTree import *
from random import randint
import time

def runContainsTest(x):
    myNums = []
    for each in range(0,x):
        myNums.append(randint(-1000,1000))
    
    myAVL = AVLTree()
    avlRoot = None
    avlRoot = myAVL.insert(avlRoot, 7)
    
    myBST = BSTree()
    bstRoot = Node(7)
    
    for elem in myNums:
        avlRoot = myAVL.insert(avlRoot, elem)
        myBST.insert(bstRoot, elem)
        
    avlStart = time.time()
    myAVL.contains(avlRoot, 100)
    avlEnd = time.time()
    print("Time for AVL: ", avlEnd-avlStart)
    
    bstStart = time.time()
    myBST.contains(bstRoot, 100)
    bstEnd = time.time()
    print("Time for BST: ",bstEnd-bstStart)
    
runContainsTest(3000)