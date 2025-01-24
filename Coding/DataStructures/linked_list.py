# Linked List Implementation

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
    def set(self, val):
        self.val = val

    def delete(self):
        self.val = None
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert(self, val):
        new = Node(val)
        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        self.size += 1

    def update(self, index, val):
        curr = self.head
        if index < self.size:
            for _ in range(index):
                curr = curr.next
            curr.set(val)
        else:
            print("Invalid index!")

    def delete(self, index):
        if index >= self.size:
            print("Invalid index!")
            return 
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        
        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev
        
        curr.delete()
        self.size -= 1

    def print(self):
        curr = self.head

        if curr:
            print(curr.val, "->", end=" ")
            while curr.next:
                curr = curr.next
                print(curr.val, "->", end=" ")
        else:
            print("Linked List is Empty")
    

l = LinkedList()
l.print()
l.insert(6)
l.insert(6)
l.insert(8)
l.update(1, 7)
l.delete(1)
l.print()



