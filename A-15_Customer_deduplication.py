"""
You are working for MNC Bank Ltd. There is a customer id list file (data/CustomerIdFile.csv). It may 
contains duplicate customer ids . Write a Python program to remove duplicate customer ids
"""
import csv

with open('data/CustomerIDFile.csv', 'a+', newline='') as f:
    f.seek(0,0)
    reader = csv.reader(f)
    id = []
    ids = []
    for row in reader:
        if row[0] not in ids:
            id.append(row)
            ids.append(row[0])
    f.seek(0,0)
    f.truncate()
    writer = csv.writer(f)
    writer.writerows(id)