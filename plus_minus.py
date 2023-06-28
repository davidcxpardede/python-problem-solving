'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

Function Description
Complete the plusMinus function in the editor below. plusMinus has the following parameter(s):
- int arr[n]: an array of integers

Print
Print the ratios of positive, negative, and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal. The function should not return a value.

Input Format
The first line contains an integer, n, the size of the array. The second line contains n space-separated integers that describe arr[n].

Constraints
0 < n <= 100
-100 <= arr[i] <= 100

Output Format
Print the following 3 lines, each to 6 decimals:
1. Proportion of positive values
2. Proportion of negative values
3. Proportion of zeros

'''


'''
SOLUTIONS PLANNING

1. Check each number in the array whether it is positive, negative, or zero.
2. For each category, create an integer variable that increments each time it is detected.
3. Print the results of each increment divided by the number of the array.
4. Make sure the division has six decimal place.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    
    positiveCount = 0       # Count of Positive Numbers
    negativeCount = 0       # Count of Negative Numbers
    zeroCount = 0           # Count of Zeroes
    
    # The following loop inspects each element in arr, and increment the counts based on its value.
    for i in arr:
        if i > 0:
            positiveCount += 1
        elif i < 0:
            negativeCount += 1
        else:
            zeroCount += 1
    
    # The following code prints the counts divided by the length of arr, while making sure it has precisely 6 decimal places.
    print(format((positiveCount/len(arr)),'.6f'))
    print(format((negativeCount/len(arr)),'.6f'))
    print(format((zeroCount/len(arr)),'.6f'))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

'''
New Things I Learned:

1. You can set the decimal places (precision) by using format. The syntax is:
format(a, '.bf')
where a is the number and b is the decimal place you want to set.
'''