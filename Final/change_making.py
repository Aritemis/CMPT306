def change_making(d, n): 
    coins = []
    largest = max(d)
    while n > 0:
        if largest <= n:
            coins.append(largest)
            n -= largest
        else:
            d.remove(largest)
            largest = max(d)
    return coins

if __name__ == "__main__":
    d = [1,2,3]
    n = 10
    print(change_making(d,n))