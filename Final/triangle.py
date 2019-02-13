
def triangle(board): 
    rows = len(board)
    minCost = board.copy()
    for i in range(1, rows):
        for j in range(len(board[i])):
            smallest = float("inf")
            if j > 0:
                smallest = min(smallest, board[i - 1][j - 1])
            if j < len(board[i]) - 1:
                smallest = min(smallest, board[i - 1][j])
            if j < len(board[i]) - 2:
                smallest = min(smallest, board[i - 1][j + 1])
            minCost[i][j] += smallest
    result = float("inf")
    for x in range(rows):
        result = min(result, minCost[rows - 1][x])
    return result

if __name__ == "__main__":
    board = [[2],[5,4],[1,4,7],[8,6,9,6]]
    print(triangle(board))