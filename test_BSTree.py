from BSTree import Node, BSTree
import unittest

class testBSTree(unittest.TestCase):
    
  
    def test_insert(self):
        someNums = [4, 9, 10, 3, 2, 15, 43, 21, 1, 54, 40, 4]
        myBST = BSTree()
        root = Node(5)
        for x in someNums:
            myBST.insert(root, x)
        actualArray = myBST.arrayHelper(root)
        desiredArray = [1, 2, 3, 4, 4, 5, 9, 10, 15, 21, 40, 43, 54]
        self.assertEqual(desiredArray, actualArray)
        
    def test_remove(self):
        #Depends on insert being performed correctly too
        someNums = [4, 9, 10, 3, 2, 15, 43, 21, 1, 54, 40, 4]
        myBST = BSTree()
        root = Node(5)
        for x in someNums:
            myBST.insert(root, x)
        toRemove = [9, 4, 42, 40, 68, 21]
        for y in toRemove:
            myBST.remove(root,y)
        actualArray = myBST.arrayHelper(root)
        desiredArray = [1, 2, 3, 4, 5, 10, 15, 40, 43, 54]
        self.assertEqual(desiredArray, actualArray)
    
    def test_contains(self):
        someNums = [4, 9, 10, 3, 2, 15, 43, 21, 1, 54, 40, 4]
        myBST = BSTree()
        root = Node(5)
        for x in someNums:
            myBST.insert(root, x)
        self.assertEqual(myBST.contains(root, 15), True)
        self.assertEqual(myBST.contains(root, 40), True)
        self.assertEqual(myBST.contains(root, 69), False)
        self.assertEqual(myBST.contains(root, 30), False)
        self.assertEqual(myBST.contains(root, 5), True)
        
        
        
if __name__ == '__main__':
    unittest.main()