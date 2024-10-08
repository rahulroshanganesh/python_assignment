"""
Assignment 8: String Manipulation
Write a Python program to count the number of strings where the string length is 2 or more and the first 
and last character are same from a given list of strings.
For Example:
Input                           Output
['abc', 'xyz', 'aba', '1221']   2
"""

def find(s):
    count = 0
    for i in s:
        if len(i)>=2 and i[0] == i[-1]:
            count += 1
    print(count)

find(['abc', 'xyz', 'aba', '1221'])