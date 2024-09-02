inp = []
m = 0

for i in range(4):
    a = int(input("Enter number: "))
    if a > m:
        m = a
    inp.append(a)

print("First maximum element in the list")
print(m)
print("Input list")
print(inp)
print("Removing the maximum element in the list")
inp.remove(m)


sec_m = 0
for i in inp:
    if i > sec_m:
        sec_m = i

print("Input list")
print(inp)
print("Second maximum element is: ", sec_m)

