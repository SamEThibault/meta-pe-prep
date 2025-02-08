# Recursion Example
def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)
# Time complexity: O(N)
# Space complexity: O(N)
# Generally, recursive runtimes end up being O(#branches^ depth)

# To figure out if a problem requires a recursive solution, look out for:
# - Choices, which item should I try first?
# - Superlatives: biggest, longest, shortest, best, all of
# - Divide and conquer: can you solve for parts separately?

# Keep in mind space complexity:
# - Every time a solution is recursive, space complexity increases because stuff is added to the call stack

# Other example
# ITERATIVE approach
def walk(steps):
    for step in range(1, steps + 1):
        print(f"Taking step {step}")
walk(10)

# RECURSIVE approach
def walk(steps):
    if steps == 0:
        return
    walk(steps - 1)
    print(f"Taking step {steps}")
walk(10)

# Here's how it works:
# - Each time you invoke a function, a frame is added to the call stack
# - So we add frames until the base condition is met
# - Since a stack is FIFO, we get the results of the newest call first
# How I think of it is: you get the function calls pushed to the stack, none of them execute
# until the function returns from the base case. Then, that first return means the top function on the call stack
# has the returned result it needs to compute its result, so on and so forth.