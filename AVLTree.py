from random import randint

class Node(object):
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.height = 1
        
        
class AVLTree():
    
    def insert(self, node, element):

        if not node:
            #at bottom of tree
            return Node(element)
        
        if element < node.element:
            node.left = self.insert(node.left,element)
        else:
            node.right = self.insert(node.right, element)

        #update height
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right)) 
    
        balanceFactor = self.getBalanceFactor(node)
        if abs(balanceFactor) > 1:
            node = self.balance(node, element, balanceFactor)
        

        return node
        
        
    def remove(self, node, element):
        #Node is the root of some subtree of the AVLTree
        if not node:
            return node
        
        elif node.element < element:
            node.right = self.remove(node.right, element)
        elif node.element > element:
            node.left = self.remove(node.left, element)
        
        #element = current node's element
        else:
            #3 types of deletion: leaf, node w 1 child, node w 2 children
            
            if node.left is None:
                tempNode = node.right
                node = None
                return tempNode
                
            elif node.right is None:
                tempNode = node.left
                node = None
                return tempNode
                
            
            temp = self.findMin(node.right)
            node.element = temp.element
            node.right = self.remove(node.right, temp.element)
        
        if node is None:
            return node
            
        #height change
        self.updateHeight(node)
        
        balanceFactor = self.getBalanceFactor(node)
        
        if balanceFactor > 1 and self.getBalanceFactor(node.left) >= 0:
            return self.singleRotateRight(node)
        
        if balanceFactor < -1 and self.getBalanceFactor(node.right) <= 0:
            return self.singleRotateLeft(node)   
        
        if balanceFactor > 1 and self.getBalanceFactor(node.left) < 0:
            node.left = self.singleRotateLeft(node.left)
            return self.singleRotateRight(node)
        
        if balanceFactor < -1 and self.getBalanceFactor(node.right) > 0:
            node.right = self.singleRotateRight(node.right)
            return self.singleRotateLeft(node)
       
        return node
    
    
    def contains(self, node, element):
        if node == None:
            return False
        if element == node.element:
            return True
        if element < node.element:
            return self.contains(node.left, element)
        else:
            return self.contains(node.right, element)
    
    def findMin(self, node):
        if node == None:
            return node
        while node.left!=None:
            node = node.left
        return node
        
    def balance(self, node, element, balanceFactor):
        
        #print(node.element, ": balanceFactor: ", balanceFactor)
        #LL
        if balanceFactor > 1 and  element < node.left.element: 
            return self.singleRotateRight(node)
  
        #RR 
        if balanceFactor < -1 and element > node.right.element: 
            return self.singleRotateLeft(node) 
  
        #left right
        if balanceFactor > 1 and element > node.left.element: 
            node.left = self.singleRotateLeft(node.left) 
            return self.singleRotateRight(node) 
  
        #right left
        if balanceFactor < -1 and element < node.right.element: 
            node.right = self.singleRotateRight(node.right) 
            return self.singleRotateLeft(node) 
  
        return node

    def singleRotateLeft(self, root): 
  
        new = root.right 
        temp1 = new.left 
  
        #rotate
        new.left = root 
        root.right = temp1 
  
        self.updateHeight(root)
        self.updateHeight(new)
        
        # Return the new root 
        return new
  
    def singleRotateRight(self, root): 
        new = root.left
        temp2 = new.right 
  
        #rotate 
        new.right = root
        root.left = temp2 
 
        self.updateHeight(root)
        self.updateHeight(new)
  
        # Return the new root 
        return new 
  
    def getHeight(self, root): 
        if root == None: 
            return 0
        return root.height 
    
    def updateHeight(self, node):
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
  
    def getBalanceFactor(self, root): 
        if not root: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    
    
    #Functions to help with testing and printing tree
    def arrayHelper(self, root):
        myElems = []
        self.arrayInOrder(root, myElems)
        return myElems
    def arrayInOrder(self, node, myArray):
        if node !=None:
            self.arrayInOrder(node.left, myArray)
            myArray.append(node.element)
            self.arrayInOrder(node.right, myArray)
        
    def heightHelper(self, root):
        myHeight = []
        self.heightsInOrder(root, myHeight)
        return myHeight
        
    def heightsInOrder(self, node, myHeights):
        if node !=None:
            self.heightsInOrder(node.left, myHeights)
            myHeights.append(node.height)
            self.heightsInOrder(node.right, myHeights)