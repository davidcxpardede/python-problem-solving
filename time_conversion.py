'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note:
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Function Description
Complete the timeConversion function. It should return a new string representing the input time in 24 hour format.
timeConversion has the following parameter:
- string s: a time in 12 hour format

Returns
- string: the time in a 24 hour format

Input Format
A single string s that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

Constraints
- All imput times are valid.

SOLUTION PLANNING
1. The concern is the first two and last two characters in the string.
2. The last two characters (AM or PM) will determine whether it is the first or second half of the day.
3. First, check if the first two characters are 12 or not.
    - If it is not 12:
        - Return the first six characters if the last two characters are AM.
        - Return the first two characters added by 12, followed by the next four characters, if the last two characters are PM.
    - If it is 12:
        - Return the first six characters if the last two characters are PM.
        - Return the first six characters, but change the first two into 00, if the last two characters are AM.
4. You must be able to check each individual string.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = s[0] + s[1]
    time = s[8] + s[9]
    hourInt = int(hour)
    
    military = ''
    
    if hourInt != 12:
        if time == 'AM':
            military = s[:8]
        else:
            hourInt += 12
            milHour = str(hourInt)
            military = milHour + s[2:8]
    else:
        if time == 'PM':
            military = s[:8]
        else:
            military = '00' + s[2:8]
    
    return(military)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

'''
NEW THINGS I LEARNED
You can trim a string (taking its middle characters) by specifying the starting and ending point of the trim.

string[a:b]
Where a is the number of first characters you want to trim, and b is the number of characters counted from the first one that you want to be left out (the remaining will be trimmed).

For example, in a string s = 'ABCDEFGH',
you can:
1. Take out its first two characters
    s[2:] -> 'CDEFGH'
2. Take out its last two characters
    s[:6] -> 'ABCDEF'
3. Do both
    s[2:6] -> 'CDEF'
As well as other amount of characters within the length of the string.
'''