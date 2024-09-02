"""
Assignment 6: String Manipulation
Given two strings S1 and S2, return a new string that contains the first, middle and lst characters of both 
strings.
• Input: 
o America
o Japan
• Output:
o AJrpan
"""

s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
s3 = s1[0]+s2[0]+s1[len(s1)//2]+s2[len(s2)//2:]

print("Inputted string1: ",s1)
print("Inputted string2: ",s2)

print("Resulting string after opertion: ", s3)
