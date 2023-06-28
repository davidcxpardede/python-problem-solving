'''
Comparison Sorting
Quicksort usually has a running time of n X log(n) but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat n x log(n) (worst-case) running time, since n X log(n) represents the minimum number of comparisons needed to know where to place each element.

Alternative Sorting
Another sorting method, the counting sort, does not require comparison. Instead, you can create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

SOLUTION PLANNING
1. Create a list of one hundred zeroes called countingArr. The index will be the same as the number the element corresponds to.
2. Iterate through the whole arr.
3. For each iteration, take the value of the element in arr.
4. Set that value as an index to the countingArr, and increment one for the iteration.
5. This means that for every number n found in arr, the n-th elements in countingArr is counted (added by 1 every time it happens). 
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    
    # Defining the frequency list
    countingArr = [0]*100
    
    # Counting the frequency of each number
    for i in range(len(arr)):
        countingArr[arr[i]] += 1
    
    return countingArr
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
