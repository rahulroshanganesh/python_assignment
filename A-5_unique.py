"""
Assignment 5: Find unique elements across two lists
Write a Python program to do the following:
• Accept lengths L1 and L2 for two lists from the user.
• Create List A of length L1 and ensure that there are no repeating elements
• Create List B of length L2 and ensure that there are no repeating elements
• Perform the following:
o Create list C that contains elements common to lists A and B.
o Create list D that contains elements unique to lists A and B.
o Print list C
o Print list D
o Print C sorted in ascending order.
o Print D sorted in descending orde
"""
import random

length1 = int(input("Enter the length of the list1: "))
length2 = int(input("Enter the length of the list2: "))

l1 = random.sample(range(length1),length1)
print("Randomly generated List1 based on length1: ", l1)
l2 = random.sample(range(length2), length2)
print("Randomly generated List1 based on length2: ",l2)

listC = []
listD = []

for x in l1:
    for y in l2:
        if x in l2 and y in l2:
            listC.append(x)
            
print("The list contains elements COMMON to lists A and B: ", list(set(listC)))
for x in l1:
    if x not in listC:
        listD.append(x)
for y in l2:
    if y not in listC:
        listD.append(y)

print("The list contains elements UNIQUE to lists A and B: ",listD)