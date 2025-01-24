# Queue implementation

class Queue:

    def __init__(self, capacity):
        self.store = [None] * capacity
        self.size = 0
        self.capacity = capacity
    
    def push(self, val):
        if self.size == self.capacity:
            print("Queue full!")
            return
        
        self.store[self.size] = val
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            print("Queue empty!")
            return
        
        item = self.store[0]
        

        for i in range(self.size - 1):
            self.store[i] = self.store[i+1]

        self.size -= 1
        return item
    
    def display(self):
        for i in range(self.size):
            print(f"({self.store[i]}) ", end="")

queue = Queue(3)
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()
queue.display()
