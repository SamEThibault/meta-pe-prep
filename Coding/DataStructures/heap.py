# Heaps
# - Specialized binary tree-based data structure used for priority-based operations
# - Max-Heap: value of each parent node is greater than or equal to its children (root is greatest)
# - Min-Heap: value of each prent node is less than or equal to its children (root is lowest)

# Completeness:
# - A heap is always a "nearly complete" binary tree, meaning all levels are filled except possibly the last,
#   which is filled from left to right

# The height of a heap is O(logN) because of its completeness property.

# Heaps are usually represented in lists.
import heapq

li = [1, 2, 3, 4, 5, 6, 7, 8]
heapq.heapify(li) # converts list to heap
print(li)

# Assuming 0-indexed array:
# arr[(i-1)/2] = Parent node of node i
# arr[(2*i) + 1] = left child node of node i
# arr[(2*i) + 2] = right child node of node i

