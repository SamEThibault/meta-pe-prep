"""
Given a vector/ array and 2 numbers, eg 2 and 5. 
Between those 2 positions in the vector (2 and 5) reverse the order of the elements
"""

def partial_reverse(array, start, end):
    if start < 0 or end > len(array) - 1:
        return False

    # we're in range, let's do it
    while start < end:
        # original approach:
        # temp = array[start]
        # array[start] = array[end]
        # array[end] = temp

        # pythonic swap:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return True

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
partial_reverse(array, 1, 8)
print(array)