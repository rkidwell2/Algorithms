from collections import defaultdict

class graphRepre():
    def __init__(self):
        self.data = defaultdict(dict)
        self.numNodes = None
        
    
def buildAdjList(filename):

    """
    This function will take a .gr file as a parameter and form an adjacency list from it.
    The adj list will be a dictionary where each key is a node in the graph and each value 
    is another dictionary. Within the smaller dictionary, each key is the neighboring node ID and 
    each value is the weight from that ID to the outer key  
    
    Adjaceny list is not redunant. edges are only listed once, as that is how the files are structured
    """
    
    f = open(filename, "r")
    
    line = f.readline()
    
    graphRep = graphRepre()
    
    while line:
        
        lineList = line.split()
        if len(lineList) != 4:
            line = f.readline()
            continue
        elif lineList[0] == "a":
            key = int(lineList[1])
            target = int(lineList[2])
            distance = int(lineList[3])
            
            graphRep.data[key][target] = distance
            
            #edges[key, target] = distance
        elif lineList[0] == "p":
            numNodes = int(lineList[2])
            graphRep.numNodes = numNodes
        
        line = f.readline()
    
   # myAdjList.graph = graphRep
   # myAdjList.distances = edges
    
    return graphRep

myList = buildAdjList('sample.gr')
#print(len(myList))

#for y in range(0,8):
    #print(myList[y])
