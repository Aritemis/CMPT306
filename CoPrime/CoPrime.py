'''
    CoPrime.py

    Generates a graph of co-primes for m x n
    
    Ariana Fairbanks
'''

import sys

'''
generates the co-primes in an m x n matrix
'''
def coprimes(m, n):
    '''
    creates a list of size m each with
    each element initialized to None
    '''
    result = [None] * (m + 1)

    '''
    each element in the list is now a
    list of size n where each value
    is initialized to a space ' '
    '''
    for i in range(0,m+1):
        result[i] = ['^'] * (n + 1)

    for j in range(0,m+1):
        l = m - j
        for k in range(0, n + 1):
            if(coprime(j+1, k+1)):
                result[l][k] = "* "
            else:
                result[l][k] = "  "


        
    '''
    output the contents of result
    '''
    for x in result:
        # x[:] is a list "slice"
        for y in x[:]:
            '''
            by putting a comma at the end, we prevent a newline
            '''
            print(y + ' ', end="")
            
        print() 

    
def getGCD(a, b):
    if(a < b):
        c = b
        b = a
        a = c
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return getGCD(a, b) == 1

# behaves like main() method

if __name__ == "__main__":
    # some error checking
    if len(sys.argv) != 3:
        print('Usage\n python CoPrime [int] [int]')
        quit()

    coprimes(int(sys.argv[1]), int(sys.argv[2]))
