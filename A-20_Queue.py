"""
Assignment 20: Custom Queue
Create a custom queue implementation using Python lists that will support the following functionalities:
• Put (add item to queue)
• Get (remove item from queue)
• Get_size (get number of elements in the queue)
• Is_empty (return True if the queue does not contain any elements)
• Truncate (remove all elements from the queue)
"""
l=[]

def put(var):
    l.append(var)

def get():
    l.remove(l[0])
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
    put(i)

print("Size of the list: ", get_size())
print("Remove item in the list: ", get())
print("Check if queue is empty: ", is_empty())
print("Remove all the item in the list: ", truncate())
print("Check if queue is empty: ", is_empty())