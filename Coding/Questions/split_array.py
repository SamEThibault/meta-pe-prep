"""
    Given an array of integers greater than zero, find if it is possible to split it in two (without reordering the elements)
    such that the sum of the two resulting arrays is the same. Print the resulting arrays
"""
def split(array):
    left_sum = 0
    right_sum = sum(array)

    for i in range(len(array) - 1):
        left_sum += array[i]
        right_sum -= array[i]
        if left_sum == right_sum:
            print(array[:i+1], array[i+1:])
    
    return False

split([1, 2, 3, 4, 5, 15])