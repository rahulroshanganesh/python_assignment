"""Create a Singly Linked List"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while(current_node!=None and current_node.next.next != None):
            current_node = current_node.next
        
        current_node.next = None

    def display(self):
        current_node = self.head
        while (current_node):
            print(current_node.data)
            current_node = current_node.next

llist = SingleLinkedList()
llist.insert_at_end('a')
llist.insert_at_end('b')
llist.insert_at_first('c')
llist.insert_at_first('d')

print("Node Data")
llist.display()

print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()

print("Node Data")
llist.display()