"""
In a given array, rotate a part of the array for which the index is given
"""

# Assumptions: give the index for the last element that should be rotated, rotate by 1 clockwise
def rotate(array, index):
    if index >= len(array):
        return False

    og = array[:index + 1]
    
    for i in range(index + 1):
        array[(i + 1) % (index + 1)] = og[i]


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotate(array, 3)
print(array)