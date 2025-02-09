# Hash table with chaining


class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

    def delete(self):
        self.key = None
        self.val = None
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.store = [None] * capacity
        self.capacity = capacity

    def insert(self, key, val):
        node = Node(key, val)
        curr = self.store[self._hash(key)]

        # If the slot is empty
        if curr is None:
            self.store[self._hash(key)] = node
            return

        while curr.next != None:
            if curr.key == key:
                print("ERROR: DUPLICATE KEY")
                return
            curr = curr.next
        curr.next = node
        return

    def delete(self, key):
        curr = self.store[self._hash(key)]

        if curr is None:
            print("KEY does not exist")
            return

        prev = None
        while curr != None:
            if curr.key == key:
                if prev and curr.next:
                    prev.next = curr.next
                elif curr.next:
                    self.store[self._hash(key)] = curr.next
                elif prev:
                    prev.next = None
                else:
                    self.store[self._hash(key)] = None
                curr.delete()
                return
            prev = curr
            curr = curr.next
        print("KEY does not exist")
        return

    def retrieve(self, key):
        curr = self.store[self._hash(key)]

        if curr is None:
            print("KEY does not exist")
            return

        while curr != None:
            if curr.key == key:
                return curr.val
            curr = curr.next
        print("KEY does not exist")
        return

    def _hash(self, key):
        return key % self.capacity

    def display(self):
        for item in self.store:
            if item is None:
                print("EMPTY")
                continue
            curr = item
            while curr is not None:
                print(f"{{{curr.key} : {curr.val}}}", end=" -> ")
                curr = curr.next
            print()


hash_table = HashTable(3)
hash_table.insert(1, 1)
hash_table.insert(4, 2)
hash_table.insert(0, 3)
hash_table.delete(1)
hash_table.delete(4)
hash_table.display()
