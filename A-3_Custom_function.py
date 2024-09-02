"""
Assignment 3: Custom function
Write a Python function that does the following:
• Accept a variable number of arguments.
• Return the following:
o Sum of all the numbers
o Average
o Maximum value
o Minimum value
"""

def math(*args):
    return sum(args), sum(args)//len(args), max(args), min(args)

s, avg, ma, mi = math(10, 20, 30)
print(f"The sum is {s}.\nThe average is {avg}.\nThe Maximum value is {ma}.\nThe Minimum value passed is {mi}.")