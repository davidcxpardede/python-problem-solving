'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals. For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9

The left-to-right diagonal = 1 + 5 + 9 = 15.
The right to left diagonal = 3 + 5 + 9 = 17.
Their absolute difference is |15 - 17| = 2.

Function Description
diagonalDifference takes the following parameter:
- int arr[n][m]: an array of integers
It returns an integer, the absolute diagonal difference.

SOLUTION PLANNING
1. Find the size of the square matrix (M X M).
2. For every size of M, the  coordinate of primary diagonal is the same: [0,0], [1,1], up to [M-1, M-1].
3. For every size of M, the coordinate of the secondary diagonal is the same on the y-axis, but the x-axis is the subtraction of the y-axis from the size: [0, M-1-0], [1, M-1-1], up to [M-1, M-1 - (M-1)].
4. After each diagonal coordinate is defined, calculate the sum and absolute difference.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    M = len(arr)
    
    # Defining and Calculating Primary Diagonal
    primaryDiagonal = 0
    secondaryDiagonal = 0
    for i in range(M):
        primaryDiagonal += arr[i][i]
        secondaryDiagonal += arr[i][M-1-i]   
    
    absoluteDiff = abs(primaryDiagonal - secondaryDiagonal)
    return absoluteDiff
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
NEw THINGS I LEARNED
1. Ranges in a for loop is excluded. For example, if you write:
for i in range(10):
It will only iterate from 0 to 9. So the upper boundary is not included.
2. For a two-dimensional matrix, the first index refers to the row, and the second index refers to the column.'''