# Dictionaries:
# - Collection of key-value pairs
# - Takes each key, hash it, % by table capacity, and that's the hash table index
# - Collisions: when 2 hashes point to the same spot in the table
# - To avoid these, there's multiple methods:
#   - Chaining: If we collide, make bucket point to a new bucket to store the new val (create linked list)
#   - Linear Probing: If we collide, linearly search for the next available slot
#   - Quadratic Probing: same idea, but use quadratic function to determine next probe position
#   - Double Hashing: When collision is found, apply second hash function to calculate offset

# In Python, the keys must be an immutable type: strings, numbers, tuples
# Hashing becomes more expensive when key data types increase in complexity

# Instead of dicts, you can also use sets:
{1, 2, 3} # Keeps track of keys, not linked to a value

# Dictionary methods:
d = {}
d.clear() # clear all elements
d.copy() # return copy of dict
d.get() # param is key, returns value of specified key
d.items() # returns list containing a typle for each key value pair
d.pop() # removes element with specified key
d.popitem() # returns last inserted key-val pair
d.setdefault("key", "value") # returns value of specified key, if key doesn't exist, insert the key with specified val
d.update() # update dict with key-val pairs
d.values() # returns list of values in dict

# Ordered Dictionaries
# LRU Cache example
from collections import OrderedDict

class LRUCache:

    # just sets capacity
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        return

    def get(self, key: int) -> int:
        # if it exists, move to end of dict, and return val
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # if it exists, move to end of dict
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            # it doesn't exist yet, check capacity
            if len(self.cache) == self.capacity:
                # if we're at capacity, pop LRU (front of dict)
                self.cache.popitem(last=False)
                
        self.cache[key] = value

