"""
Assignment 4: List Operations
Consider the following list:
numbers = [1,2,3,4,5,1,2,3,4,5,1,2,3,1,2,1,2,3,4,5]
Write a Python program to do the following:
• Display the first and last element in the list
• If element '2' is present, print PRESENT, else print NOT PRESENT
• Print the count of occurrence of element 4
"""
numbers = [1,2,3,4,5,1,2,3,4,5,1,2,3,1,2,1,2,3,4,5]
print("first element is: ", numbers[0])
print("Last element is: ", numbers[-1])
print("**********************************")

if 2 in numbers:
    print("PRESENT")
else:
    print("NOT PRESENT")
print("**********************************")

print("count of 4 in numbers is: ", numbers.count(4))
print("**********************************")