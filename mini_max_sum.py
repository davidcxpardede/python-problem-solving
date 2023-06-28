'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''
'''
SOLUTION PLANNING

RANDOM METHOD
1. Randomly add four of the five integers and store its value.
2. Do the first step for the next set of four.
3. Compare the values. Retain the highest one.
4. Finish the iteration until all combinations have been calculated.
5. The last highest value is the maximum possible value.
6. Repeat the steps above for the minimum value.

SORTED METHOD
1. Sort the array in ascending order.
2. The maximum value is the sum of the last four elements.
3. The minimum value is the sum of the first four elements.

I will go with the SORTED METHOD as it is more efficient.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort() # Sorting arr in ascending order
    
    # Defining min and max by adding the first and last four values of arr, respectively
    min = arr[0] + arr[1] + arr[2] + arr[3]
    max = arr[1] + arr[2] + arr[3] + arr[4]
    
    # Printing the value of min and max
    print(f"{min} {max}")
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    
'''
NEW THINGS I LEARNED

To sort an array, use the following function:
arr.sort()
Where arr is the arr name.
You can add the parameter to do it in descending order:
arr.sort(reverse=True)
By default, without any parameters, it is sorting in ascending order.
This is also applicable in an array of strings or characters, where it will be sorted in alphabetical order.
'''