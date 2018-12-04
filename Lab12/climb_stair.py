
def climb_stair(n):
    result = [i for i in range(0, n+1)]
    for i in range(4, n+1):
        result[i] = result[i - 1] + result[i - 2]
    return result[n]

if __name__ == "__main__":
    print(climb_stair(10))
    print(climb_stair(20))
    print(climb_stair(30))
