"""
Write a Python function that takes a list of numbers and determines if all the numbers are unique. If yes, 
return TRUE, else return FALSE.
"""
import random
a = random.sample(range(5), 5)

def unique_list(a):
    s = []
    for i in a:
        if i not in s:
            s.append(i)
        else:
            return False 
    return True

print(a)
b = a.copy()
b.append(4)
print(b)

if unique_list(a):
    print("Lista is unqiue")
else:
    print("Lista is not unique")

if unique_list(b):
    print("Listb is unqiue")
else:
    print("Listb is not unique")