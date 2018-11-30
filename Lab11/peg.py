from copy import deepcopy as copy
import argparse
from animation import draw

class Node():
    def __init__(self, board, jumpfrom = None, jumpover = None, jumpto = None):
        self.board = board
        self.jumpfrom = jumpfrom
        self.jumpover = jumpover
        self.jumpto = jumpto

class peg:
    def __init__(self, start_row, start_col, rule):
        self.size = 5
        self.start_row, self.start_col, self.rule = start_row, start_col, rule
        # board
        self.board = [[1 for j in range(i+1)] for i in range(self.size)]
        self.board[start_row][start_col] = 0
        self.start = Node(copy(self.board))
        # path
        self.path = []

        self.temp = 0
        self.visited = []



    def draw(self):
        if self.success():
            draw(self.path, self.start_row, self.start_col, self.rule)
        else:
            print("No solutions were found.")

    def success(self):
        pegs = 0
        success = False
        for row in range(0, self.size):
            for col in range(0, row + 1):
                if self.board[row][col] == 1:
                    pegs += 1
        if pegs == 1:
            if self.rule == 0 or self.board[self.start_row][self.start_col] == 1:
                success = True

        return success
        
    def solve(self, node):
        
        if self.temp == 25:
            return False

        #self.temp += 1

        if node is None:
            node = Node(copy(self.board))

        #print(node.board)
        
        if self.success():
            self.path.insert(0, node)
            return True
        
        for row in range(0, self.size):
            rowMO = row - 1
            rowMT = row - 2
            rowPO = row + 1
            rowPT = row + 2
            for col in range(0, row + 1):
                if self.board[row][col] == 1:
                    colMO = col - 1
                    colMT = col - 2
                    colPO = col + 1
                    colPT = col + 2
                    if (row > 1) and (col < (rowMO)) and (self.board[rowMT][col] == 0) and (self.board[rowMO][col] == 1):
                        newBoard = copy(self.board)
                        newBoard[row][col] = 0
                        newBoard[rowMO][col] = 0
                        newBoard[rowMT][col] = 1
                        if newBoard in self.visited:
                            return False
                        self.visited.append(newBoard)
                        self.board = copy(newBoard)
                        newJumpfrom = (row, col)
                        newJumpover = (rowMO, col)
                        newJumpto = (rowMT, col)
                        if self.solve(Node(copy(self.board), newJumpfrom, newJumpover, newJumpto)):
                            self.path.insert(0, node)
                            return True
                    if (row > 1) and (col < (rowMO)) and (self.board[row][colPT] == 0) and (self.board[row][colPO] == 1):
                        newBoard = copy(self.board)
                        newBoard[row][col] = 0
                        newBoard[row][colPO] = 0
                        newBoard[row][colPT] = 1
                        if newBoard in self.visited:
                            return False
                        self.visited.append(newBoard)
                        self.board = copy(newBoard)
                        newJumpfrom = (row, col)
                        newJumpover = (row, colPO)
                        newJumpto = (row, colPT)
                        if self.solve(Node(copy(self.board), newJumpfrom, newJumpover, newJumpto)):
                            self.path.insert(0, node)
                            return True
                    if (row < 3) and (self.board[rowPT][colPT] == 0) and (self.board[rowPO][colPO] == 1):
                        newBoard = copy(self.board)
                        newBoard[row][col] = 0
                        newBoard[rowPO][colPO] = 0
                        newBoard[rowPT][colPT] = 1
                        if newBoard in self.visited:
                            return False
                        self.visited.append(newBoard)
                        self.board = copy(newBoard)
                        newJumpfrom = (row, col)
                        newJumpover = (rowPO, colPO)
                        newJumpto = (rowPT, colPT)
                        if self.solve(Node(copy(self.board), newJumpfrom, newJumpover, newJumpto)):
                            self.path.insert(0, node)
                            return True
                    if (row < 3) and (self.board[rowPT][col] == 0) and (self.board[rowPO][col] == 1):
                        newBoard = copy(self.board)
                        newBoard[row][col] = 0
                        newBoard[rowPO][col] = 0
                        newBoard[rowPT][col] = 1
                        if newBoard in self.visited:
                            return False
                        self.visited.append(newBoard)
                        self.board = copy(newBoard)
                        newJumpfrom = (row, col)
                        newJumpover = (rowPO, col)
                        newJumpto = (rowPT, col)
                        if self.solve(Node(copy(self.board), newJumpfrom, newJumpover, newJumpto)):
                            self.path.insert(0, node)
                            return True
                    if (col > 1) and (self.board[row][colMT] == 0) and (self.board[row][colMO] == 1):
                        newBoard = copy(self.board)
                        newBoard[row][col] = 0
                        newBoard[row][colMO] = 0
                        newBoard[row][colMT] = 1
                        if newBoard in self.visited:
                            return False
                        self.visited.append(newBoard)
                        self.board = copy(newBoard)
                        newJumpfrom = (row, col)
                        newJumpover = (row, colMO)
                        newJumpto = (row, colMT)
                        if self.solve(Node(copy(self.board), newJumpfrom, newJumpover, newJumpto)):
                            self.path.insert(0, node)
                            return True
                    if (col > 1) and (self.board[rowMT][colMT] == 0) and (self.board[rowMO][colMO] == 1):
                        newBoard = copy(self.board)
                        newBoard[row][col] = 0
                        newBoard[rowMO][colMO] = 0
                        newBoard[rowMT][colMT] = 1
                        if newBoard in self.visited:
                            return False
                        self.visited.append(newBoard)
                        self.board = copy(newBoard)
                        newJumpfrom = (row, col)
                        newJumpover = (rowMO, colMO)
                        newJumpto = (rowMT, colMT)
                        if self.solve(Node(copy(self.board), newJumpfrom, newJumpover, newJumpto)):
                            self.path.insert(0, node)
                            return True
        
        if node.jumpfrom != None:
            print(node.jumpfrom)
            print(node.jumpover)
            print(node.jumpto)
            print()
            self.board[node.jumpfrom[0]][node.jumpfrom[1]] = 1
            self.board[node.jumpover[0]][node.jumpover[1]] = 1
            self.board[node.jumpto[0]][node.jumpto[1]] = 0
            
        return False


        
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='peg game')

    parser.add_argument('-hole', dest='position', required = True, nargs = '+', type = int, help='initial position of the hole')
    parser.add_argument('-rule', dest='rule', required = True, type = int, help='index of rule')

    args = parser.parse_args()

    start_row, start_col = args.position
    if start_row > 4:
        print("row must be less than or equal to 4")
        exit()
    if start_col > start_row:
        print("column must be less than or equal to row")
        exit()

    # Example: 
    # python peg.py -hole 0 0 -rule 0
    game = peg(start_row, start_col, args.rule)
    game.solve(None)
    game.draw()
    