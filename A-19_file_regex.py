"""
Write a python program using regular expressions that does the following:
• Read lines from file A
• If the line begins with a capital letter:
o Write all the words in that line that start with a vowel to file B – one per line.
o Write all words that contain numbers to file C – one per line.
o Write all words that do not start or end with ‘a’ but contain ‘a’ to file D – one per line.
• Print the longest word in file A.
• Print the longest word in file B.
"""

import csv
import re

a = []
fileD=[]
d = {}
count = 0
l = 0
s= ''
with open('data/A-19.txt', 'r') as f:
    reader = csv.reader(f)
    writer = csv.writer(f)
    vowel = ['a', 'e', 'i', 'o', 'u']
    for row in reader:
        if row[0][0][0].isupper():
            val = row[0].split()
            count += 1
            for item in val:
                if re.match('[aeiou]', item[0]):
                    d["fileB"+str(count)] = row
        if re.match('[0-9]',row[0]):
            a.append(row)
        val = row[0].split()
        for item in val:
            if not( (item.startswith('a') or item.startswith('A')) or (item.endswith('a') or item.endswith('A')) ):
                if 'a' in item:
                    fileD.append(item)
            if len(item) > l:
                l = len(item)
                s = item


# Temp storage to write in the file.
# print(d)
# print(a)
# print(fileD)
print("Longest Word in file A: ",s)
t = 0
c = ''
for y in a:
    for x in y:
        v = x.split()
        for im in v:
            if len(im) > t:
                t = len(im)
                c = im
print("Longest Word in file B: ",im)

f = open('fileB.txt', 'w')
for row in d.values():
    f.writelines(row[0])
    f.write("\n")
f.close()

f = open('fileC.txt', 'w')
for row in a:
    f.writelines(row[0])
    f.write("\n")
f.close()

f = open('fileD.txt', 'w')
for row in fileD:
    f.writelines(row)
    f.write("\n")
f.close()