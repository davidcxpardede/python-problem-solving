'''
''Given an array of integers, where all elements but one occur twice, find the unique element.

Function Description
The function returns an integer (element that occurs only once).

SOLUTION PLANNING
1. Sort the array.
2. Check if the first element is the same as the second element. If it is not, the first element is the lonely integer.
3. Iterate through each element starting from the second element up to the second-to-last. 
4. For each iteration, check whether it is different with the previous or next element.
5. If both conditions are met, that element is the lonely integer. Otherwise, continue iterating.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    a.sort()
    l = len(a)
    lonelyInteger = 0
    
    if l == 1:
        lonelyInteger = a[0]
    else:
        if a[0] != a[1]:
            lonelyInteger = a[0]
        elif l == 3:
            lonelyInteger = a[2]
        else:
            for i in range(1, l-2):
                if (a[i] != a[i-1]) and (a[i] != a[i+1]):
                    lonelyInteger = a[i]
                    break
                else:
                    lonelyInteger = a[l-1]
    
    return lonelyInteger

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()''
