
def roll_dice(N,M):
    t = [[0] * (M + 1) for _ in range(N + 1)]
    t[0][0] = 1
    for i in range(1, N + 1):
        for j in range(i, min(M, i * 6) + 1):
            for k in range(1, min(6, j) + 1):
                t[i][j] += t[i - 1][j - k]
    return t[N][M]

if __name__ == "__main__":
    print(roll_dice(2,7))
    print(roll_dice(3,9))
    print(roll_dice(8,24))
