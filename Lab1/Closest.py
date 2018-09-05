'''
Closest pair problem

This returns the closest pair of numbers.

Usage:
    
    python closest_pair.py [size of list of numbers]

@author Ariana Fairbanks

@date August 2018
'''

import random
import sys

'''
return the distance between two parameters
'''
def distance(a,b):
    return abs(a-b)


'''
populate the array with listSize unique random numbers between 1 ... 5000
'''
def populate(listSize):
    a = []
    count = 0

    while count < listSize:
        number = random.randint(1,5000)
        if number in a:
            continue
        else:
            a.append(number)
            count += 1

    return a

'''
now determine the closest pair
using brute force algorithm
'''
def closest_pair(values):
   
    if len(values) < 2:
        return (0, 0)


    pt_a = values[0]
    pt_b = values[1]
    dis = abs(pt_a - pt_b)

    for i in range(len(values)):
        current_a = values[i]
        for j in range(len(values)):
            if j != i:
                current_b = values[j]
                current_dis = abs(current_a - current_b)
                if current_dis < dis:
                    dis = current_dis
                    pt_a = current_a
                    pt_b = current_b


    return (pt_a, pt_b)

'''
This behaves just like the Java main() method
'''
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage Python closest_pair.py [number of points]')
        quit()
    else:
        numbers = populate(int(sys.argv[1]))

        closest = closest_pair(numbers)

        print('The closest numbers are', closest[0], 'and', closest[1])
