"""
    Given an array of integers greater than zero, find if it is possible to split it in two (without reordering the elements)
    such that the sum of the two resulting arrays is the same. Print the resulting arrays
"""

def split(array):

    i = len(array) // 2 # start at mid point
    left_sum = sum(array[:i])
    right_sum = sum(array[i:])
    visited = {}

    while 0 <= i < len(array) - 1:
        print(visited)
        print(i)
        print(left_sum)
        print(right_sum)
        print("###################")
        if visited.get(i, 0):
            return False
        if left_sum < right_sum:
            left_sum += array[i]
            right_sum -= array[i]
            visited[i] = 1
            i += 1
        elif left_sum > right_sum:
            right_sum += array[i]
            left_sum -= array[i]
            visited[i] = 1
            i -= 1
        else:
            left = array[:i]
            right = array[i:]
            print(left, right)
            return True

split([4, 4, 8])