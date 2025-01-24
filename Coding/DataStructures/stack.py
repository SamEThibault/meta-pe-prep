# Stack implementation

class Stack:

    def __init__(self, capacity):
        self.store = [None] * capacity
        self.size = 0
        self.capacity = capacity
    
    def push(self, val):
        if self.size == self.capacity:
            print("Stack full!")
            return
        
        self.store[self.size] = val
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            print("Stack empty!")
            return
        
        item = self.store[self.size - 1]
        self.size -= 1
        return item
    
    def display(self):
        for i in range(self.size):
            print(f"({self.store[i]}) ", end="")

stack = Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.push(4)
stack.display()
