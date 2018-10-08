

class TopologicalSorting:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a directed graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
        # file name
        self.name = fileName
        
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
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)
        
        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()
        self.unVisitedVertices = list(set(self.vertices))    
        self.unVisitedVertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

        # sorted list
        self.sortedList = []

    def p_a_s(self, file):
        print(self.vertices)
        print(self.adjacencyList)
        self.sort()
        print(self.sortedList)

        with open(str(file), 'w') as file_handler:
            for node in self.sortedList:
                file_handler.write("{}\n".format(node)) 

    def print_and_save(self):
        #print(self.vertices)
        #print(self.adjacencyList)
        self.sort()
        print(self.sortedList)

        with open('results-'+ str(self.name), 'w') as file_handler:
            for node in self.sortedList:
                file_handler.write("{}\n".format(node)) 
        

    # Topological sorting using decrease-by-one-and-conquer. 
    def sort(self):
        while self.unVisitedVertices:
            pathless = list(set(self.unVisitedVertices))    
            pathless.sort()
            for vertex in self.adjacencyList:
                for v in self.adjacencyList[vertex]:
                    if v in pathless:
                        pathless.remove(v)
            self.unVisitedVertices.remove(pathless[0])
            if pathless[0] in self.adjacencyList:
                del self.adjacencyList[pathless[0]]
            self.sortedList.append(pathless[0])



    # Finish this function for extra credit
    # How many different ways can the spider reach the fly by moving along the web’s lines in the directions indicated by the arrow?
    def spider(self):
        # Your code goes here:
        pass


if __name__ == "__main__":

    #s = TopologicalSorting("graph-example.txt")
    #s.print_and_save()
    #s = TopologicalSorting("c:/Users/My LENOVO/Desktop/other workspace/CMPT306/Lab7/graph-example.txt")
    #s.p_a_s("c:/Users/My LENOVO/Desktop/other workspace/CMPT306/Lab7/graph-example-results.txt")

    #s = TopologicalSorting("graph-courses.txt")
    s = TopologicalSorting("c:/Users/My LENOVO/Desktop/other workspace/CMPT306/Lab7/graph-courses.txt")
    s.p_a_s("c:/Users/My LENOVO/Desktop/other workspace/CMPT306/Lab7/graph-courses-results.txt")
    #s.print_and_save()

    #s = TopologicalSorting("graph-spider.txt")
    #s = TopologicalSorting("c:/Users/My LENOVO/Desktop/other workspace/CMPT306/Lab7/graph-spider.txt")
    #s.print_and_save()
    print("Done")