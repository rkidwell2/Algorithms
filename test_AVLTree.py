from AVLTree import AVLTree, Node
import unittest
from random import randint

class testAVLTree(unittest.TestCase):
    def test_insert(self):
        """
        For insertion, we must test that each possible rebalancing that could be triggered will create the correct tree
        If the smallest cases work, all others should work too
        """
        
        myAVL = AVLTree()
        myRoot = None
        
        #test for single left rotate rebalance
        testNums = [1, 2, 3]
        for each in testNums:
            myRoot = myAVL.insert(myRoot, each)
        self.assertEqual(myAVL.arrayHelper(myRoot), [1,2,3])
        self.assertEqual(myAVL.heightHelper(myRoot), [1,2,1])
        self.assertEqual(myRoot.element, 2)
        
        #test for single right rotate rebalance
        
        myAVL = AVLTree()
        myRoot = None
        
        testNums = [3, 2, 1]
        for each in testNums:
            myRoot = myAVL.insert(myRoot, each)
        self.assertEqual(myAVL.arrayHelper(myRoot), [1,2,3])
        self.assertEqual(myAVL.heightHelper(myRoot), [1,2,1])
        self.assertEqual(myRoot.element, 2)
        
        #test for double left rotate rebalance
        
        myAVL = AVLTree()
        myRoot = None
        
        testNums = [1, 3, 2]
        for each in testNums:
            myRoot = myAVL.insert(myRoot, each)
        self.assertEqual(myAVL.arrayHelper(myRoot), [1,2,3])
        self.assertEqual(myAVL.heightHelper(myRoot), [1,2,1])
        self.assertEqual(myRoot.element, 2)
        
        #test for double right rotate rebalance
        myAVL = AVLTree()
        myRoot = None
        
        testNums = [3, 1, 2]
        for each in testNums:
            myRoot = myAVL.insert(myRoot, each)
        self.assertEqual(myAVL.arrayHelper(myRoot), [1,2,3])
        self.assertEqual(myAVL.heightHelper(myRoot), [1,2,1])
        self.assertEqual(myRoot.element, 2)
        
    def test_remove(self):
        #Test the smallest possible trees that require each type of rotation
        #single left rotate test
        myAVL = AVLTree()
        myRoot = None
        
        testNums = [2, 3, 1, 4]
        for each in testNums:
            myRoot = myAVL.insert(myRoot, each)
        myRoot = myAVL.remove(myRoot, 1)
        self.assertEqual(myAVL.arrayHelper(myRoot), [2,3,4])
        self.assertEqual(myAVL.heightHelper(myRoot), [1,2,1])
     
        
        #single right rotate test
        myAVL = AVLTree()
        myRoot = None
        
        testNums = [3, 2, 4, 1]
        for each in testNums:
            myRoot = myAVL.insert(myRoot, each)
        myRoot = myAVL.remove(myRoot, 4)
        self.assertEqual(myAVL.arrayHelper(myRoot), [1,2,3])
        self.assertEqual(myAVL.heightHelper(myRoot), [1,2,1])
        
        #double left rotate test
        myAVL = AVLTree()
        myRoot = None
        
        testNums = [2, 4, 1, 3]
        for each in testNums:
            myRoot = myAVL.insert(myRoot, each)
        myRoot = myAVL.remove(myRoot, 1)

        self.assertEqual(myAVL.arrayHelper(myRoot), [2,3, 4])
        self.assertEqual(myAVL.heightHelper(myRoot), [1,2,1])
        self.assertEqual(myRoot.element, 3)
        self.assertEqual(myRoot.left.element, 2)
        self.assertEqual(myRoot.right.element, 4)
        
        #double right rotate
        myAVL = AVLTree()
        myRoot = None
        
        testNums = [3, 1, 4, 2]
        for each in testNums:
            myRoot = myAVL.insert(myRoot, each)
        myRoot = myAVL.remove(myRoot, 4)

        self.assertEqual(myAVL.arrayHelper(myRoot), [1, 2, 3])
        self.assertEqual(myAVL.heightHelper(myRoot), [1,2,1])
        self.assertEqual(myRoot.element, 2)
        self.assertEqual(myRoot.left.element, 1)
        self.assertEqual(myRoot.right.element, 3)
    
    def test_containts(self):
        myAVL = AVLTree()
        myRoot = None
        
        testNums = []
        for x in range(0,100):
            testNums.append(randint(0,200))
        for each in testNums:
            myRoot = myAVL.insert(myRoot, each)
            
        self.assertEqual(myAVL.contains(myRoot, testNums[7]), True)
        self.assertEqual(myAVL.contains(myRoot, testNums[34]), True)
        self.assertEqual(myAVL.contains(myRoot, testNums[99]), True)
        self.assertEqual(myAVL.contains(myRoot, testNums[56]), True)
        self.assertEqual(myAVL.contains(myRoot, 400), False)
        self.assertEqual(myAVL.contains(myRoot, -12), False)
        
if __name__ == '__main__':
    unittest.main()