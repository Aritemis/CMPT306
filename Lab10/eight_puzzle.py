import numpy as np
from heapq import heappush, heappop
from animation import draw
import argparse

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
    
    def __init__(self, start_state, goal_state, method, algorithm, array_index):
        self.start_state = start_state
        self.goal_state = goal_state
        self.visited = [] # state
        self.method = method
        self.algorithm = algorithm
        self.m, self.n = start_state.shape 
        self.array_index = array_index   

    def goal_test(self, current_state):
        return np.array_equal(current_state, self.goal_state)

    def get_cost(self, current_state, next_state):
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

    def heuristics(self, state):
        priority = 0
        if self.method == "Manhattan":
            for row in range(0,3):
                for col in range(0,3):
                    endNumber = self.goal_state[row,col]
                    currentRow, currentCol = np.where(state == endNumber)
                    priority += abs(row - currentRow)
                    priority += abs(col - currentCol)
        elif self.method == "Hamming":
            for row in range(0,3):
                for col in range(0,3):
                    endNumber = self.goal_state[row,col]
                    currentRow, currentCol = np.where(state == endNumber)
                    if row != currentRow or col != currentCol:
                        priority += 1
        return priority

    # priority of node 
    def priority(self, node):
        priority = 0
        if self.algorithm == "UCS":
            self.method = "Manhattan"
            priority = node.cost_from_start + self.heuristics(node.state)
        elif self.algorithm == "Greedy":
            priority = self.heuristics(node.state)
        elif self.algorithm == "AStar":
            priority = node.cost_from_start + self.heuristics(node.state)

        return priority
    
    # draw 
    def draw(self, node):
        path=[]
        while node.parent:
            path.append(node.state)
            node = node.parent
        path.append(self.start_state)

        draw(path[::-1], self.array_index, self.algorithm, self.method)
            
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

        elif self.algorithm == 'Greedy': 
            heappush(container, (count, count, node))
        
        elif self.algorithm == 'AStar': 
            heappush(container, (count, count, node))

        while container:
            if self.algorithm == 'Depth-Limited-DFS':
                currentNode = container.pop()
            elif self.algorithm == 'BFS': 
                currentNode = container[0]
                container.remove(currentNode)            
            elif self.algorithm == 'UCS':
                currentNode = heappop(container)[2]
            elif self.algorithm == 'Greedy':
                currentNode = heappop(container)[2]
            elif self.algorithm == 'AStar':
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

                    elif self.algorithm == 'Greedy': 
                        count += 1
                        heappush(container, (self.priority(nextNode), count, nextNode))

                    elif self.algorithm == 'AStar': 
                        count += 1
                        heappush(container, (self.priority(nextNode), count, nextNode))

if __name__ == "__main__":
    
    goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
    start_arrays = [np.array([[1,2,0],[3,4,6],[7,5,8]]),
                    np.array([[8,1,3],[4,0,2],[7,6,5]])]
    methods = ["Hamming", "Manhattan"]
    algorithms = ['Depth-Limited-DFS', 'BFS', 'UCS', 'Greedy', 'AStar']
    
    parser = argparse.ArgumentParser(description='eight puzzle')

    parser.add_argument('-array', dest='array_index', required = True, type = int, help='index of array')
    parser.add_argument('-method', dest='method_index', required = True, type = int, help='index of method')
    parser.add_argument('-algorithm', dest='algorithm_index', required = True, type = int, help='index of algorithm')

    args = parser.parse_args()

    # Example:
    # Run this in the terminal using array 0, method Hamming, algorithm AStar:
    #     python eight_puzzle.py -array 0 -method 0 -algorithm 4
    game = EightPuzzle(start_arrays[args.array_index], goal, methods[args.method_index], algorithms[args.algorithm_index], args.array_index)
    game.solve()