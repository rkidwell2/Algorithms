from readGraph import buildAdjList
import math

class node():
    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.dist = distance

class minHeap():       
    
    def __init__(self):
        self.myArr = []
        self.size = 0
        
        """
        Create array to keep track of the minheap position of each vertex
        example: if myArr = [[4, 10], [2, 17], [5, 10], [0, 10000], [6, 10000], [5, 10], [6, 10000]]
                (heap is really only size 4 because others have been "removed")
            then indexs =   [3, 6, 1, 5, 0, 2, 4]
                    as vertex 0 is at index 3 in the priority queue, vertex 2 is at index 1 in the heap, 
                    vertex 4 is at index 0 in the priority queue, etc. 
        """
        self.indexs = [] 
        
    def getParent(self,index):
        return (index-1)//2
    def leftChild(self, index):
        return index*2 + 1 
    def rightChild(self, index):
        return index*2 + 2 
        
    def minheapify(self, index):
        #index is index of subtree's root
        
        #val = self.myArr[index].dist #store index dist value to use as comparison
        
        leftI = self.leftChild(index)
        rightI = self.rightChild(index)
        
        minIndex = index #put min as index, then see if needs to be changed
        
        if leftI < self.size and self.myArr[leftI].dist < self.myArr[minIndex].dist:
            #If a left child exists and the distance there is less than the current distance..
            #print("comparing ", val, "and ", self.myArr[leftI])
            minIndex = leftI
            
        if rightI < self.size and self.myArr[minIndex].dist > self.myArr[rightI].dist:
            #If right child exists and is less than current minimum, change right to be minimum
            minIndex = rightI
            
        if minIndex!=index:
            #Swap position
            self.indexs[self.myArr[minIndex].vertex] = index 
            self.indexs[self.myArr[index].vertex] = minIndex
            
            #Need to swap nodes
            self.myArr[index], self.myArr[minIndex] = self.myArr[minIndex], self.myArr[index]
            #print("swapped ", self.myArr[index], "and", self.myArr[minIndex])
            self.minheapify(minIndex)
            
    def removeMin(self):
        #Function to return the minimum (vertex, distance) pair and remove it from the heap
        #If heap is empty, return
        if self.size == 0:
            return
        
        #print("array before extraction: ", self.myArr)
        root = self.myArr[0]
        
        #move last node to the top
        final = self.myArr[self.size-1]
        self.myArr[0] = final
        
  
        #update index reference array
        self.indexs[final.vertex] = 0
        self.indexs[root.vertex] = self.size -1
     
        
        #reduce size of heap
        self.size -= 1
        #heapify the root
        
        self.minheapify(0)
        
        return root
        
    def decreaseKey(self, vertx, newDist):
        #Decrease distance key of a vertex, passing the (vertex, distance) pair and min heapify
        #Will be called from Dijkstra

        #index of vertex in myArr
        i= self.indexs[vertx]
        self.myArr[i].dist = newDist
        
        #until at top of heap or until node in correct position
        parent = self.getParent(i)
        while i != 0 and self.myArr[i].dist < self.myArr[parent].dist:
        
            self.indexs[self.myArr[i].vertex] = parent
            self.indexs[self.myArr[parent].vertex] = i
    
            self.myArr[i], self.myArr[parent] = self.myArr[parent], self.myArr[i]

            i = self.getParent(i)
            parent = self.getParent(i)
   
        self.minheapify(i)
    
    def buildMinHeap(self, adjList):
        """
        Function to build the initial min heap from the adjacency list
        """
        num_v = len(adjList)
        
        for x in range(0, num_v+2):
            self.indexs.append(x)
            y = node(x, math.inf)
            self.myArr.append(y)
        
    
    def print_info(self):
        print("Min heap: ")
        for x in self.myArr:
            print("{", x.vertex, ", ", x.dist, " },")
        print("heap size: ", self.size)
        print("postion array: ", self.indexs)

class dijkstraSol():
    def __init__(self):
        self.distanceArray = []
        self.predecessors = []
        self.src = 0

def dijkstra(graph, src):
    #Takes in an adjacency list graph representation and source node as input
    #returns distance and path to all other nodes
    heap = minHeap()
    #Initialize array to keep track of total distances
    distances = []
    
    #Initialize array to keep track of predecessor node
    preds = []
    
    num_v = graph.numNodes
    adjDict = graph.data
    
    heap.buildMinHeap(adjDict)
    heap.size = num_v+1
    
    for y in range(0,num_v+1):
        distances.append(math.inf)
        preds.append(None)
   
    #Set source to be at top of heap and distance to be zero   
    heap.decreaseKey(src, 0)
    heap.indexs[src] = src ###maybe needed 
    
    distances[src] = 0
    
    #Start going through every node until the min heap is empty
    while heap.size != 0:
        #extract min
        currNode = heap.removeMin()
        u = currNode.vertex
        
        neighbors = adjDict[u]
        for v in neighbors:
        
            #Check to see if neighbor is still in the min heap
            inheap = heap.indexs[v] < heap.size

            if inheap and distances[u] != math.inf and distances[v] > adjDict[u][v] + distances[u]:
                distances[v] = adjDict[u][v] + distances[u]
                preds[v] = u
                
                heap.decreaseKey(v, distances[v])
    
    mySol = dijkstraSol()
    mySol.distanceArray = distances
    mySol.predecessors = preds
    mySol.src = src
    
    return mySol
         
         
def create_output(inputfile, src , target):
    
    reading = buildAdjList(inputfile)
    djSol = dijkstra(reading, src)
    
    file_name = "Dijkstra_for_" + str(djSol.src) + "_to_" + str(target)
    
    f = open(file_name, "w")
    totalWeight = djSol.distanceArray[target]
    
    if totalWeight == math.inf:
        f.write("There is no solution from node %d to node %d" % (src, target))
        return
    
    f.write(str(totalWeight) +"\n")
    
    list_of_preds = []
    curr = target
    while curr != src:
        list_of_preds.insert(0,curr)
        curr = djSol.predecessors[curr]
    
    list_of_preds.insert(0, curr)
    
    for each in list_of_preds:
        f.write(str(each) + "\n")
    
    return
    
create_output('nymap.gr', 1, 1276)

