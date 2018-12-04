
def change_making(d,n):
	result = [0 for i in range(0, n+1)]
	for i in range(1, n+1):
		smallest = float("inf")
		for j in range(0, len(d)):
			if (d[j] <= i):
				smallest = min(smallest, result[i - d[j]]) 
		result[i] = 1 + smallest 
	return result[n]

if __name__ == "__main__":
    d = [1,3,4,5,6]
    n = 10
    print(change_making(d,n))
    
    d = [1,2,4,6,8,10,22,23]
    n = 40
    print(change_making(d,n))

    d = [1,2,10,11,12,15,19,30]
    n = 1900
    print(change_making(d,n))

