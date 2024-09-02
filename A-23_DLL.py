"""Create Doubly linked list"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None

    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        if current_node.prev is not None:
            current_node.prev.next = None
        else:
            self.head = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

dllist = DoublyLinkedList()
dllist.insert_at_end('a')
dllist.insert_at_end('b')
dllist.insert_at_first('c')
dllist.insert_at_first('d')

print("Node Data")
dllist.display()

print("\nRemove First Node")
dllist.remove_first_node()
print("Remove Last Node")
dllist.remove_last_node()

print("Node Data")
dllist.display()
