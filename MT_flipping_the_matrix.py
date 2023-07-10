'''
Sean invented a game involving a 2n X 2n matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the n X n submatrix located in the upper-left quadrant of the matrix.
Given the initial configurations for q matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.

SOLUTION PLANNING

CASE #1
For a 2X2 matrix, simply find the elements with the highest value.

CASE #2
For 4X4 matrix and larger, define the maximum value for each possible flip.

The top-left quadrant Q of 2n X 2n matrix M will be a square matrix of the size n.
- The first element (top-left element) of the Q matrix can only be placed by the corner elements of M ([0,0], [0, 2n-1], [2n-1, 0], [2n-1, 2n-1].
- The last element (bottom-right element) of the Q matrix can only be placed by the core elements of M ([n-1,n-1], [n-1,n-1+1],[n-1+1,n-1],[n-1+1,n-1+1])
- Overall, the flippable elements of a n X n matrix is the combination of the following.

    1 2 3 4 5 6     1 2 3
    1 2 3 4 5 6     1 2 3
    1 2 3 4 5 6     1 2 3
    1 2 3 4 5 6
    1 2 3 4 5 6
    1 2 3 4 5 6
                                        [2][0]
    [0],[2n-1]      [0],[2n-1-1]     ...     [0],[n-1-(n-1+1)]
    [1],[2n-1]      [1],[2n-1-1]     ...     [1],[n-1-(n-1+1)]
    ...             ...              ...     ...
    [n-1],[2n-1]    [n-1],[2n-1-1]   ...     [n-1],[n-1-(n-1+1)]
    
    The general equation for an i and j iteration will be:
    
    [i],[2n-1-j]
    
With that general formula, we can find the maximum value for each elements in Q by iterating through all possible combination.
For each maximum value found, store and increment it to get the maximum sum possible.
'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    dimension = int(len(matrix)/2)
    
    maximumQuadrantSum = 0
    quadrantCombination = [0] * 4
    
    for i in range(dimension):
        for j in range(dimension):
            quadrantCombination[0] = [matrix[i][j]]
            quadrantCombination[1] = [matrix[i][len(matrix)-1-j]]
            quadrantCombination[2] = [matrix[len(matrix)-1-i][j]]
            quadrantCombination[3] = [matrix[len(matrix)-1-i][len(matrix)-1-j]]
            
            maximumQuadrantSum += max(quadrantCombination)[0]
    
    return maximumQuadrantSum
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()



