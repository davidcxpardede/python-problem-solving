'''
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y, and z would map to z, a, b, and c.

Note:
The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Function Description
caesarCipher has the following parameters:
- string s: cleartext
int k: the alphabet rotation factor
- returns string: the encrypted string

Input Format
The first line contains the integer, n, the length of the unencrypted string.
The second line contains the unencrypted string, s.
The third line contains k, the number of letters to rotate the alphabet by.

SOLUTION PLANNING:
1. Create a dictionary of alphabets from a-z.
2. Read each letter of the given string (for loop). To avoid confusion, change all the letters into lowercase.
3. For each letter, match it with the index of the letter on the dictionary. Then, add the index by the constants k, and substitute it to the original letter.
    - If the index exceeds 25 (26 - 1), rotate it back to 0.
4. Return the new string as encryptedString.
'''

import string

alphabetLower = list(string.ascii_lowercase)
alphabetUpper = list(string.ascii_uppercase)

s = "www.abc.xy"
es = list(s)
k = 87
print(es)

for i in range(len(s)):
    char = s[i]
    
    if char in alphabetLower:
        index = alphabetLower.index(char)
        if (index+k) < 26:
            es[i] = alphabetLower[index+k]
        else:
            mod = k%26
            es[i] = alphabetLower[index+mod-26]
    
    elif char in alphabetUpper:
        index = alphabetUpper.index(char)
        if (index+k) < 26:
            es[i] = alphabetUpper[index+k]
        else:
            mod = k%26
            es[i] = alphabetUpper[index+mod-26]
    else:
        es[i] = char 

encryptedString = ''.join(es)
print(encryptedString)

'''
NEW THINGS I LEARNED

1. Create alphabet:
    alphabetLower = list(string.ascii_lowercase)
    alphabetUpper = list(string.ascii_uppercase)
2. Convert a list of strings/chars into a single string:
    singleString = 'X'.join(listOfString)
    where X denotes the divider.
3. Strings are immutable in Python, which means its elements cannot be changed. If you wish to, convert it first into a list, change the element of the list, and convert back to string.
'''