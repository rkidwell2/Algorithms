import unittest
from Sorter import heapSort, quicksort, mergesort, buildArray
import time

class testSorter(unittest.TestCase):
    
    def test_mergesort(self):
        
        x = 500000
        array = buildArray(x)
        sortedArray = sorted(array)
        
        start = time.time()
        mergesort(array)
        end = time.time()
        
        print("Run time of merge sort with array of size %d is %f." %(x, end-start))
        
        self.assertEqual(array, sortedArray)
     
    def test_heapSort(self):
        
        x = 500000 #Size of array
        array = buildArray(x)
        sortedArray = sorted(array)
        
        start = time.time()
        heapSort(array)
        end = time.time()
        
        print("Run time of heap sort with array of size %d is %f." %(x, end-start))
        self.assertEqual(array, sortedArray)
    
    def test_quicksort(self):
        x = 500000
        array = buildArray(x)
        sortedArray = sorted(array)
        
        start = time.time()
        quicksort(array)
        end = time.time()
        
        print("Run time of quick sort with array of size %d is %f." %(x, end-start))
        self.assertEqual(array, sortedArray)
        
        


if __name__ == '__main__':
    unittest.main()