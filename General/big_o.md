# Big O Basics
- Ensure to define N
- Drop constants
- Defines both time complexity and space complexity with same notation

O(1) - Constant time
O(log N) - Logarithmic time
O(N) - Linear time
O(N log N) - Linearithmic time
O(N^2) - Quadratic time
O(2^N) - Exponential time
O(N!) - Factorial time

# Big O Examples

```python
def print_pairs_with_sum(array, target):
    for a in array:
        for b in array:
            if a + b == target:
                print(a, b)
```
This is an example of O(N^2), we go through the same array, N times.

If we use 2 pointers:

```python
def print_pairs_with_sum(array, target):
    for left in range(len(array)):
        for right in range(left + 1, len(array)):
            a = array[left]
            b = array[right]
            if a + b == target:
                print(a, b)
```
This is actually O((N^2)/2), but since we drop constants, it's still O(N^2).

# Tips and Tricks
- Don't ignore function runtimes
- Use logical variable names, don't just toss around the N label
- Add sequential steps, and multiply nested steps
- Biggest factor wins (assuming they're talking about the same variable)
