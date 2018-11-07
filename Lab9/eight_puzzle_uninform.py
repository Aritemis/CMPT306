import numpy as np
from heapq import heappush, heappop
from animation import draw

class Node():
    """
    cost_from_start - the cost of reaching this node from the starting node
    state - the state (row,col)
    parent - the parent node of this node, default as None
    """
    def __init__(self, state, cost_from_start, parent = None):
        self.state = state
        self.parent = parent
        self.cost_from_start = cost_from_start


class EightPuzzle():
    
    def __init__(self, start_state, goal_state, algorithm, array_index):
        self.start_state = start_state
        self.goal_state = goal_state
        self.visited = [] 
        self.algorithm = algorithm
        self.array_index = array_index

    # goal test function
    def goal_test(self, current_state):
        return np.array_equal(current_state, self.goal_state)

    # get cost function
    def get_cost(self, current_state, next_state):
        # find cost of action from current state to next state

        # We already have ready access to the cost of the previous node 
        # and the cost of a step is always one.
        # It is unclear why we even need this method or 
        # what you want it to do.

        # Your instructions are often confusing and unclear.
        return 1

    # get successor function
    def get_successors(self, state):
        successors = []
        zeroRow, zeroCol = np.where(state == 0)
        if zeroRow > 0:
            temp = state.copy()
            newRow = zeroRow - 1
            newValue = state[newRow, zeroCol]
            temp[newRow, zeroCol] = 0
            temp[zeroRow, zeroCol] = newValue
            successors.append(temp)
        if zeroRow < 2:
            temp = state.copy()
            newRow = zeroRow + 1
            newValue = state[newRow, zeroCol]
            temp[newRow, zeroCol] = 0
            temp[zeroRow, zeroCol] = newValue
            successors.append(temp)
        if zeroCol > 0:
            temp = state.copy()
            newCol = zeroCol - 1
            newValue = state[zeroRow, newCol]
            temp[zeroRow, newCol] = 0
            temp[zeroRow, zeroCol] = newValue
            successors.append(temp)
        if zeroCol < 2:
            temp = state.copy()
            newCol = zeroCol + 1
            newValue = state[zeroRow, newCol]
            temp[zeroRow, newCol] = 0
            temp[zeroRow, zeroCol] = newValue
            successors.append(temp)
        
        return successors

    # get priority of node for UCS
    def priority(self, node):
        priority = node.cost_from_start
        for row in range(0,3):
            for col in range(0,3):
                endNumber = self.goal_state[row,col]
                currentRow, currentCol = np.where(node.state == endNumber)
                priority += abs(row - currentRow)
                priority += abs(col - currentCol)
        return priority
    
    # draw 
    def draw(self, node):
        path=[]
        while node.parent:
            path.append(node.state)
            node = node.parent
        path.append(self.start_state)
        print(path)
        draw(path[::-1], self.array_index, self.algorithm)

    # solve it
    def solve(self):
        container = [] 
        count = 1
        state = self.start_state.copy()
        node = Node(state, 0, None)
        self.visited.append(state)
        if self.algorithm == 'Depth-Limited-DFS': 
            container.append(node)

        elif self.algorithm == 'BFS': 
            container.append(node)

        elif self.algorithm == 'UCS': 
            heappush(container, (count, count, node))

        while container:
            if self.algorithm == 'Depth-Limited-DFS':
                currentNode = container.pop()
            elif self.algorithm == 'BFS': 
                currentNode = container[0]
                container.remove(currentNode)            
            elif self.algorithm == 'UCS':
                currentNode = heappop(container)[2]

            if self.goal_test(currentNode.state):
                self.draw(currentNode)
                break
            
            successors = self.get_successors(currentNode.state)

            for nextState in successors:
                visited = False
                for visitedStates in self.visited:
                    if np.array_equal(visitedStates, nextState):
                        visited = True
                if not visited:
                    nextCost = currentNode.cost_from_start + self.get_cost(node.state, nextState)
                    nextNode = Node(nextState, nextCost, currentNode)
                    self.visited.append(nextState)

                    if self.algorithm == 'Depth-Limited-DFS': 
                        if nextCost < 16:
                            count += 1
                            container.append(nextNode)

                    elif self.algorithm == 'BFS': 
                        count += 1
                        container.append(nextNode)

                    elif self.algorithm == 'UCS': 
                        count += 1
                        heappush(container, (self.priority(nextNode), count, nextNode))
                    
            
            
if __name__ == "__main__":
    
    goal = np.array([[1,2,3],[4,5,6],[7,8,0]])

    start_arrays = [np.array([[0,1,3],[4,2,5],[7,8,6]]), 
                    np.array([[0,2,3],[1,4,6],[7,5,8]])] 

    algorithms = ['Depth-Limited-DFS', 'BFS', 'UCS']
    
    for i in range(len(start_arrays)):
        for j in range(len(algorithms)):
            game = EightPuzzle(start_arrays[i], goal, algorithms[j], i )
            game.solve()
