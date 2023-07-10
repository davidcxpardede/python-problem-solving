'''
Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play optimally. The rules of the game are as follows:
- Initially there are n towers.
- Each tower is of height m.
- The players move in alternating turns.
- In each turn, a player can choose a tower of height x and reduce its height to y, where 1 <= y < x and y evenly divides x.
- If the current player is unable to make a move, they lose the game.

Given the values of n and m, determine which player will win. If the first player wins, return 1. Otherwise, return 2.

Returns
int: the winner of the game.

SOLUTION PLANNING:
This case is hard enough for me to solve by myself, so I consult to a very good tutorial on YouTube.

https://www.youtube.com/watch?v=jOxTTE3IkjE&ab_channel=praveen

He uses special cases and conditions to determine who would win assuming both players make an optimal play each turn.

1. If the number of tower is 1, Player 1 always wins.
2. If the height of all towers is 1, Player 2 always wins.
3. If the number of tower is even, Player 2 always wins.
4. If the number of tower is odd, Player 1 always wins.

The code will then follow those simple rules to determine the winner.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    
    if m == 1 or n%2 == 0:
        return 2
    else:
        return 1
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

'''
NEW THINGS I LEARNED:

1. Do not rely solely on mathematical code for a solution. Sometimes, simple logic and code solves them all.
2. Try to understand the problem and break down how you can group the possible cases or results. In this problem, there are infinitely many cases which can be grouped down to ONLY four conditions. That greatly simplifies the problem.
'''