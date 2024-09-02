"""
Assignment 9: List Manipulation
Given a list of numbers, do the following:
• Divide the list into 3 slices.
• Reverse each slice and print it.
• Combine the 3 slices into a final list and print it.
• Combine the 3 slices into a list of 3 lists.
Input list L1 = [1,2,3,4,5,6,7,8,9]
Outputs:
• [3,2,1]
• [6,5,4]
• [9,8,7]
• [3,2,1,6,5,4,9,8,7]
• [[3,2,1],[6,5,4],[9,8,7]
"""

def do(s):
    a = []
    res_inv = []
    nested_res_inv = []
    i = 0
    while i!=len(s):
        a.append(s[slice(i, i+3)])
        i += 3
    for item in a:
        print(item[::-1])
        nested_res_inv.append(item[::-1])
        for val in item[::-1]:
            res_inv.append(val)
    print(res_inv)
    print(nested_res_inv)


do([1,2,3,4,5,6,7,8,9])