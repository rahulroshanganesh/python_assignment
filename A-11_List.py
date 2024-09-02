"""
Consider the following situation:
• Headings = [“first_name”, “last_name”, “age”]
• Person1 = [“Mark”,”Taylor”,20]
• Person2 = [“Emma”,”Jones”,30]
Write a Python program that will create the output dictionary where each element of the headings is the 
key and each corresponding element in person lists will be a list of values.
Output:
{'first_name': ['Mark', 'Emma'], 'last_name': ['Taylor', 'Jones'], 'age': [20, 30]}
"""

Headings = ['first_name', 'last_name', 'age']
Person1 = ['Mark','Taylor',20]
Person2 = ['Emma','Jones',30]

a = dict()
j = 0
for i in Headings:
    a[i] = [Person1[j], Person2[j]]
    j += 1
    
print(a)