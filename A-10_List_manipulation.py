"""
Given two lists of equal size, create a set that shows corresponding elements as a pair.
Input:
• L1 = [1,2,3,4,5]
• L2 = [11,22,33,44,55]
Output: S1 = {(1,11), (2,22), (3,33), (4,44), (5,55)}
"""

def con(s, m):
    z = set(zip(s, m))
    return z

print(con([1,2,3,4,5], [11,22,33,44,55]))