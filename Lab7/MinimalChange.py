'''

For example, if values = [1,2,3]
this will return:
[ (1,2,3), (1,3,2), (3,1,2), (3,2,1), (2,3,1), (2,1,3) ]

'''

import sys

def permutate(value):
    result = []
    if value > 0:
        if value == 1:
            result.append((1,))
        else:
            previous = permutate(value - 1)
            end = len(previous)
            for i in range(0, end):
                current = previous[i]
                print("current " + str(current))
                if i % 2 == 0:
                    for j in range(0, len(current) + 1):
                        result.append(current[:(len(current) - j)] + (value,) + current[(len(current) - j):])
                else:
                    for k in range(0, value):
                        result.append(current[:(k)] + (value,) + current[(k):])
    return result

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage\n python MinimalChange [int]')
        quit()

    result = permutate(int(sys.argv[1]))

    print(result)
