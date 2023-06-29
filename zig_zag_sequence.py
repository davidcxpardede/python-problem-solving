'''
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Debugging means the process of identifying and removing errors from computer hardware or software.

Debugging, in computer programming and engineering, is a multistep process that involves identifying a problem, isolating the source of the problem, and then either correcting the problem or determining a way to work around it. The final step of debugging is tot est the correction or workaround and make sure it works.

Given an array of n distinct integers, transform the array into a zig zag sequence by permuting the array elements. A sequence will be called a zig zag sequence if the first k elements in the sequence are in increasing order and the last k elements are in decreasing order, where k = (n+1)/2. You need to find the lexicographically smallest zig zag sequence of the given array.

Debug the given function findZigZagSequence to return the appropriate zig zag sequence for the given input array.

Note:
You can modify at most three lines in the given code. You cannot add or remove lines of code.
'''

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2 - 1) # MODIFIED FROM mid = int((n + 1)/2 - 1)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2      # MODIFIED FROM ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1     # MODIFIED FROM ed = ed + 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
