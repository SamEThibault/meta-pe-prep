# Arrays Basics
# Initialization:
array = []
array = [[1, 2, 3], [1, 2, 3]]

# Initialize to 0:
array = [0] * 100

# Get Length:
length = len(array)

# min/max:
minimum = min(array)
maximum = max(array)

# Sorting
array.sort() # in-place
sorted_arr = sorted(array) # deep copy

# Operations
array.append(1) # add to end
array.pop(1) # remove by index
array.remove(0) # remove specific element
array.count(1) # count occurences of element
array.index(0) # return index of element
array.insert(0, 1) # add element at specified position (ind, element)
array.reverse() # reverse the order in-place

# Partitioning
arr = [1, 2, 3, 4, 5]
even = [x for x in arr if x % 2 == 0]
odd = [x for x in arr if x % 2 != 0]

# Merging
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merged = arr1 + arr2 # [1, 3, 5, 2, 4, 6]

# Slicing
arr = [1, 2, 3, 4, 5]
sliced_arr = arr[1:4] # [2, 3, 4]

# List Comprehension
squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]

# Reduce
from functools import reduce
arr = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, arr) # 24

# Map
arr = [1, 2, 3]
doubled = list(map(lambda x: x* 2, arr)) # [2, 4, 6]

# Filter
arr = [1, 2, 3, 4]
# this needs to be cast to a list since filter() returns an iterator
even = list(filter(lambda x: x % 2 == 0, arr)) # [2, 4]

# Matrices
# Make sure you work with matrix[row][col] to avoid mistakes

#########################
# Practice
# Pair with Given Sum in a Sorted Array
def countPairs(arr, k):
  res = 0
  left, right = 0, len(arr) - 1

  while (left != right):
    s = arr[left] + arr[right]
    if (s == k):
      res += 1
      left += 1
      right -= 1
    elif (s > k):
      right -= 1
    else:
      left += 1

  return res

