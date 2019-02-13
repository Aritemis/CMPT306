import sys

class three_color():
    def __init__(self,inputFile):
        # read the file 
        graph = open(inputFile)

        self.adjacency = { }
        self.vertices = [ ]

        for line in graph:
            entry = line.split()

            # get the vertices
            self.vertices.append(entry[0])
            self.vertices.append(entry[1])

            if entry[0] not in self.adjacency:
                self.adjacency[entry[0]] = []

            self.adjacency[entry[0]].append(entry[1])

        # construct a sorted list of unknown vertices
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # color set: red, green, blue  
        self.color_set = ['R','G','B']
        
        # a set to hold the relationship between color and vertex
        self.assigncolor = {}
        for vertex in self.vertices:
            self.assigncolor[vertex] = None
        
        # call solve starting from the first vertex  
        self.solve(0)
        print(self.assigncolor)

    # check if two adjacent vertices have the same color
    def isSafe(self,index):
        # your code goes here:
        pass



    # back-tracking 
    def solve(self, index):
        # your code goes here:
        pass



        

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage python filename')
        quit()
  
    #inputFile = 'graph1.txt'
    #inputFile = 'graph2.txt'
    obj = three_color(sys.argv[1])
    