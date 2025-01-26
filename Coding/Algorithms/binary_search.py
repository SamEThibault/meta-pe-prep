# Binary Search:
# Works on sorted arrays, go to the middle, check if its lower or higher than target, 
# then split group in half and check the side that could contain the target, repeat

# This is worst case O(logN)

# Recursive approach
def binary_search(arr, target, left, right):
    if (left > right):
        return False
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
    

# Iterative approach (this works to show the algorithm, but is bad practice, use left and right index trackers instead)
def binary_search_iterative(arr, target):
    
    subarr = arr.copy()
    while len(subarr) >= 1:
        mid_i = len(subarr) // 2
        mid_val = subarr[mid_i]
        if mid_val == target:
            return True
        if mid_val > target:
            subarr = subarr[:mid_i]
        else:
            subarr = subarr[mid_i:]

    return False
        


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(binary_search(arr, 5, 0, len(arr) - 1))
print(binary_search_iterative(arr, 5))

