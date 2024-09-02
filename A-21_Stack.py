"""
Create a custom stack implementation using Python lists that will support the following functionalities:
• push (add item to stack)
• pop (remove item from stack)
• Get_size (get number of elements in the stack)
• Is_empty (return True if the stack does not contain any elements)
• Truncate (remove all elements from the stack)

"""
l=[]

def push(var):
    l.append(var)

def pop():
    l.remove(l[len(l)-1])
    return l

def get_size():
    return len(l)

def is_empty():
    if len(l) == 0:
        return True
    else:
        return False
    
def truncate():
    l.clear()

for i in range(5):
    push(i)

print("Size of the list: ", get_size())
print("Remove item in the list: ", pop())
print("Check if queue is empty: ", is_empty())
print("Remove all the item in the list: ", truncate())
print("Check if queue is empty: ", is_empty())