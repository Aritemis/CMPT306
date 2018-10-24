
'''    
@author: Ariana Fairbanks
'''

class jugs():
    def __init__(self, water, capacity, goal):
        self.water = water
        self.capacity = capacity
        self.goal = goal
        self.visited = [] # node has been explored 
        self.child_parent = {} # child is key and parent is value

    def solve(self):    
        node = self.BFS()
        result = [node]
        # retrieve a path from root to the solution node
        while node in self.child_parent:
            node = self.child_parent[node]
            result.insert(0, node)
        print(result)

    def BFS(self):
        # return the node if there is a goal in it 
        queue = [ ]
        toAdd = [ ]
        queue.append(water)
        self.visited.append(water)
        while queue:
            node = queue[0]
            if self.goal in node:
                return node
            queue.remove(node)

            a = node[0]
            b = node[1]
            c = node[2]
            aCapacity = capacity[0]
            bCapacity = capacity[1]
            cCapacity = capacity[2]
            aGreaterThan0 = a > 0
            bGreaterThan0 = b > 0
            cGreaterThan0 = c > 0
            aDifference = aCapacity - a
            bDifference = bCapacity - b
            cDifference = cCapacity - c
            aLessThanCapacity = aDifference > 0
            bLessThanCapacity = bDifference > 0
            cLessThanCapacity = cDifference > 0

            if aGreaterThan0:

                if bLessThanCapacity:
                    if a > bDifference:
                        aNew = a - bDifference
                        bNew = bCapacity
                    else:
                        aNew = 0
                        bNew = b + a
                    toAdd.append((aNew, bNew, c))
                
                if cLessThanCapacity:
                    if a > cDifference:
                        aNew = a - cDifference
                        cNew = cCapacity
                    else:
                        aNew = 0
                        cNew = c + a
                    toAdd.append((aNew, b, cNew))

            if bGreaterThan0:

                if aLessThanCapacity:
                    if b > aDifference:
                        bNew = b - aDifference
                        aNew = aCapacity
                    else:
                        bNew = 0
                        aNew = a + b
                    toAdd.append((aNew, bNew, c))
                
                if cLessThanCapacity:
                    if b > cDifference:
                        bNew = b - cDifference
                        cNew = cCapacity
                    else:
                        bNew = 0
                        cNew = c + b
                    toAdd.append((a, bNew, cNew))
                
            if cGreaterThan0:

                if aLessThanCapacity:
                    if c > aDifference:
                        cNew = c - aDifference
                        aNew = aCapacity
                    else:
                        cNew = 0
                        aNew = a + c
                    toAdd.append((aNew, b, cNew))

                if bLessThanCapacity:
                    if c > bDifference:
                        cNew = c - bDifference
                        bNew = bCapacity
                    else:
                        cNew = 0
                        bNew = b + c
                    toAdd.append((a, bNew, cNew))

            for value in toAdd:
                if value not in self.visited:
                    queue.append(value)
                    self.visited.append(value)
                    self.child_parent[value] = node

if __name__ == '__main__':

    capacity = (8,5,3)
    water = (8,0,0)
    goal = 4

    #capacity = (9,5,4)
    #water = (9,0,0)
    #goal = 3

    j = jugs(water, capacity, goal)
    j.solve()
