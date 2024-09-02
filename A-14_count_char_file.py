"""
Consider a text file.
Write a Python program that will do the following:
• Count the number of times each character – alphabets, numbers, symbols - occurs in a text file
• Print the characters and their counts in alphabetical order
• Print the characters and their counts in the descending order of their counts.
"""
d = {}

with open('1.txt', 'r') as f:
    l = f.readline()
    # print(type(l))
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

print("*******************ORIGINAL DICT*******************")
print(d)
keys = sorted(d)
print("*******************ALPHBETICAL ORDER*******************")
for i in keys:
    print(i, d[i])
print("*******************DESC ORDER based on values*******************")
new = {key:value for key, value in sorted(d.items(), key=lambda d: d[1], reverse=True)}
print(new)
