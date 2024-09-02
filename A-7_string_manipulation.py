"""
Assignment 7: String Manipulation
Write a Python function that will do the following:
• Accept a String as input argument. Example: “PythoN 3.8 is great! 40”
• Return the following values in one go:
o ythoPN is great
o 40 great! is 3.8 PythoN
o 40 !taerg si 3.8 NohtyP
o Count of numbers = 2
o Number of special characters = 1
o A dictionary of characters and their count of occurrences.
o Sum, average, minimum and maximum of all numbers in the string.
o Remove punctuation marks – PythoN 3.8 is great 40
o Retain only numbers – 3.8 40
"""

def string_mani(s):
    sen = []
    s = s.split()
    for i in s:
        if i.isalpha():
            sen.append(i)
        if i.isdigit():
            pass

    sen.append(s[3])
    for item in sen:
        cap = ''
        res = ''
        if any(char.isupper() for char in item):
            for char in item:
                if char.isupper():
                    cap += char
                else:
                    res += char
        else:
            break
        val = res + cap
    # print(val)
    sen_v = sen[0]
    sen = ' '.join(sen)
    sen = sen.replace(sen_v, val)
    

    third = []
    count = 0
    count_spl = 0  
    summm = 0
    num_l = []
    rem_pun = []
    r = ''
    d = {}

    for i in s:
        for j in i:
            if j in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]:
                count_spl += 1
            else:
                rem_pun.append(j)
            if j not in d:
                d[j] = 1
            else:
                d[j] += 1
        rem_pun.append(' ')
        if i.isalpha():
            third.append(i[::-1])
        else:
            third.append(i)
        try:
            if isinstance(int, int(i)):
                count += 1
                summm += int(i)
                num_l.append(int(i))
        except Exception as e:
            print
        try:
            if isinstance(float(i),float):
                count += 1
                summm += float(i)
                num_l.append(float(i))
        except:
            # print()
            print
        
    
    print(sen)
    print(' '.join(s[::-1]))
    third = ' '.join(third)
    print(third)
    print("Count of numbers: ")
    print(count)
    print("Count of special characters: ")
    print(count_spl)
    print("Dictionaries of characters: ")
    print(d)

    print("Sum of the numbers: ")
    print(summm)
    print("Average of the numbers: ")
    print(summm//count)
    print("list of the numbers: ")
    print(num_l)
    print("Maximum of the numbers: ")
    print(max(num_l))
    print("Minimum of the numbers: ")
    print(min(num_l))
    print("Removed puntuation")
    print(''.join(rem_pun))
    print("Only numbers")
    for r in num_l:
        print(r)
    

    


string_mani("PythoN 3.8 is great! 40")
