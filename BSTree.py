"""BinarySearchTreeclass withmethods insert(E element),
remove(E element), contains(E element)
Write a test class for BinarySearchTreeas well."""

class Node(object):
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        
class BSTree():
    
    def insert(self, node, element):
        #Node is root at first then recursively called
        newNode = Node(element)
        if node == None:
            return newNode
            
        if node.element < element:
            if node.right != None:
                self.insert(node.right, element)
            else:
                node.right = newNode
        else:
            if node.left != None:
                self.insert(node.left,element)
            else:
                node.left = newNode
        return newNode
    
    def contains(self, root, element):
        
        if root.element == element:
            return True
        elif element > root.element and root.right:
            return self.contains(root.right, element)
        elif element < root.element and root.left:
            return self.contains(root.left, element)
        else:
            return False
     
    def remove(self, node, element): 
        #will return new root (of subtree)
        if node == None:
            return node
        if node.element < element:
            node.right = self.remove(node.right, element)
        elif node.element > element:
            node.left = self.remove(node.left, element)
        else:
            #Found our node
            
            #no children, just remove node
            if node.left == None and node.right == None:
                node == None
            
            elif node.left == None:
                temp = node.right
                node = None
                return temp
            
            elif node.right == None:
                temp = node.left
                node = None
                return temp
                
            else:
                #node has both children. move largest value of left subtree to spot
                temp = node
                while temp.right != None:
                    temp = temp.right
                
                node.element = temp.element
                node.left = self.remove(node.left, temp.element)
        return node
    
    def arrayHelper(self, node):
        myArray = []
        self.arrayInOrder(node, myArray)
        return myArray
    
    def arrayInOrder(self, node, myArray):
        if node != None:
            self.arrayInOrder(node.left, myArray)
            myArray.append(node.element)
            self.arrayInOrder(node.right, myArray)


someNums = [4, 9, 10, 3, 2, 15, 43, 21, 1, 54, 40, 4]
myBST = BSTree()
root = Node(5)
for x in someNums:
    myBST.insert(root, x)
toRemove = [9, 4, 42, 40, 68, 21]
for y in toRemove:
    myBST.remove(root,y)



# #Test for contains method
# someMoreNums = [4, 9, 6, 30, 10, 3, 2, 65, 15]
# for x in someMoreNums:
#     print("is " , x, "in this tree?...", myBST.contains(root, x))

