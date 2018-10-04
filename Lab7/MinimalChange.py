'''

For example, if values = [1,2,3]
this will return:
[ (1,2,3), (1,3,2), (3,1,2), (3,2,1), (2,3,1), (2,1,3) ]

'''

import sys

def permutate(value):
    result = []
    first = []
    second = []
    if value > 0:
        for i in range(1, value):
            first.append(i)
            second.insert(0,i)
        for j in range(0, value):
            current = first.copy()
            current.insert((value - 1 - j), value)
            if tuple(current) not in result:
                result.append(tuple(current))
        for k in range(0, value):
            current = second.copy()
            current.insert(k, value)
            if tuple(current) not in result:
                result.append(tuple(current))

        
          
    return result






if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage\n python MinimalChange [int]')
        quit()

    result = permutate(int(sys.argv[1]))

    print(result)
