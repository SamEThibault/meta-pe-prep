"""
    Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrive the key's value at the nearest timestamp
    https://leetcode.com/problems/time-based-key-value-store/description/
"""

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.store.get(key, False):
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store.get(key, False)
        if vals and vals[0][1] <= timestamp:
            # Binary Search to find closest timestamp
            left, right = 0, len(vals) - 1
            best_val = vals[0][0]

            while left <= right:
                mid = (left + right) // 2
                if vals[mid][1] == timestamp:
                    return vals[mid][0]

                if vals[mid][1] > timestamp:
                    right = mid - 1
                else:
                    best_val = vals[mid][0]
                    left = mid + 1

            return best_val
        return ""
 