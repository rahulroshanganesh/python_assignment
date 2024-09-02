"""
There are two sets of country codes:
• S1 = {"US","IN","NL"}
• S2 = {"CA","IN","BE"}
Write a Python program that will do the following:
• Print a common set of country codes.
• Print all country codes across two sets sorted in descending order.
Outputs:
• {'IN'}
• ['US', 'NL', 'IN', 'CA', 'BE']
"""

S1 = {"US","IN","NL"}
S2 = {"CA","IN","BE"}

print(S1.intersection(S2))
res = list(S1.union(S2))
res.sort(reverse=True)
print(res)