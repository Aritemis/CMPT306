def matrix(board): 
    rows = len(board)
    cols = len(board[0])
    minCost = board.copy()
    for i in range(1, rows):
        for j in range(cols):
            smallest = board[i - 1][j]
            if j > 0:
                smallest = min(smallest, board[i - 1][j - 1])
            if j < cols - 1:
                smallest = min(smallest, board[i - 1][j + 1])
            minCost[i][j] += smallest
    result = float("inf")
    for x in range(rows):
        result = min(result, minCost[rows - 1][x])
    return result

if __name__ == "__main__":
    board = [[1,2,3],[4,5,6],[7,0,2]]
    print(matrix(board))