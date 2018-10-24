'''    
@author: Ariana Fairbanks
'''

from itertools import permutations
import math
import numpy as np

class GraphAlgorithms:

    def __init__(self, fileName): 
    
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graphFile:
            '''
            Get the two vertices and the cost
            '''
            (firstVertex, secondVertex, cost) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)
            
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = { }
        
            self.adjacencyList[firstVertex][secondVertex] = cost
            #self.adjacencyList[secondVertex][firstVertex] = cost

        graphFile.close()

        self.vertices = list(set(self.vertices))
        self.vertices.sort()
    
    def solve(self):
        min_cost = np.inf # initialize global min_cost as infinity
        min_path = "" # initialize min_path as empty

        places = len(self.vertices)
        permutationString = ""

        for i in range(0,places):
            permutationString = permutationString + str(i)

        for path in permutations(permutationString):
            pathString = ""
            cost = 0
            currentPlace = ""
            previousPlace = ""
            lastPlace = ""

            first = True
            for point in path:
                currentPlace = self.vertices[int(point)]
                pathString = pathString + currentPlace + " -> "
                if first:
                    lastPlace = currentPlace
                    first = False
                else:
                    cost += int(self.adjacencyList[previousPlace][currentPlace])
                previousPlace = currentPlace

            pathString = pathString + lastPlace
            cost += int(self.adjacencyList[previousPlace][lastPlace])
            
            #print(str(cost) + " " + pathString)

            if cost < min_cost:
                min_cost = cost
                min_path = pathString

        #print()
        #print(self.adjacencyList)
        #print()

        return min_cost, min_path

if __name__ == '__main__':
    g = GraphAlgorithms('vt.txt')
    #g = GraphAlgorithms("c:/Users/My LENOVO/Desktop/other workspace/CMPT306/Midterm/vt.txt")
    print(g.solve())
    