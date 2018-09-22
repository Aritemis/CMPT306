import sys

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
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

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

    def Init(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))        
        # initialize path as an empty string
        self.path = ""

    '''
    depth-first traversal of specified graph
    '''
    def DFS(self, method):
        self.Init()
        if method is 'recursive':
            start = self.vertices[0]
            self.DFS_recur(start)
            if self.unVisitedVertices:
                self.unVisitedVertices.sort()
                self.DFS_recur(self.unVisitedVertices[0])
            return self.path

        elif method is 'stack':
            self.DFS_stack(self.vertices[0])
            if self.unVisitedVertices:
                self.unVisitedVertices.sort()
                self.DFS_stack(self.unVisitedVertices[0])
            return self.path   

    def DFS_recur(self, vertex):
        self.path = self.path + vertex
        self.unVisitedVertices.remove(vertex)
        for adjacents in self.adjacencyList[vertex]:
            if adjacents in self.unVisitedVertices:
                self.DFS_recur(adjacents)
                
    def DFS_stack(self, vertex):
        stack = [ ]
        stack.append(vertex)
        while stack:
            current = stack.pop()
            if current in self.unVisitedVertices:
                self.path = self.path + current
                self.unVisitedVertices.remove(current)
                for adjacents in self.adjacencyList[current]:
                    if adjacents in self.unVisitedVertices:
                        stack.append(adjacents)

    def BFS(self):
        self.Init()
        self.BFS_run(False)
        if self.unVisitedVertices:
            self.unVisitedVertices.sort()
            self.BFS_run(True)
        return self.path

    def BFS_run(self, repeat):
        queue = [ ]
        first = self.vertices[0]
        if repeat:
            first = self.unVisitedVertices[0]
        queue.append(first)
        self.unVisitedVertices.remove(first)
        while queue:
            current = queue[0]
            queue.remove(current)
            self.path = self.path + current
            for adjacents in self.adjacencyList[current]:
                if adjacents in self.unVisitedVertices:
                    self.unVisitedVertices.remove(adjacents)
                    queue.append(adjacents)

    def hasCycle(self):
        self.Init()
        cycle = self.findCycle(self.vertices[0])
        if cycle == False and self.unVisitedVertices:
            self.unVisitedVertices.sort()
            cycle = self.findCycle(self.unVisitedVertices[0])
        return cycle

    def findCycle(self, vertex):
        parent = { }
        stack  = [ ]
        stack.append(vertex)
        parent[vertex] = None
        self.unVisitedVertices.remove(vertex)
        while stack:
            current = stack.pop()
            for adjacents in self.adjacencyList[current]:
                if adjacents in self.unVisitedVertices:
                    stack.append(adjacents)
                    self.unVisitedVertices.remove(adjacents)
                    parent[adjacents] = current
                elif adjacents != parent[current]:
                    print(current + " " + adjacents + " " + parent[current])
                    return True
        return False
        
    def shortestpath(self, p, q):
        self.Init()
        queue = [ ]
        queue.append(p)
        levelMap = { }
        levelMap[p] = 0
        self.unVisitedVertices.remove(p)
        while queue:
            current = queue[0]
            currentLevel = levelMap[current] + 1
            queue.remove(current)
            for adjacents in self.adjacencyList[current]:
                if adjacents == q:
                    return currentLevel
                if adjacents in self.unVisitedVertices:
                    self.unVisitedVertices.remove(adjacents)
                    levelMap[adjacents] = currentLevel
                    queue.append(adjacents)
        return 0