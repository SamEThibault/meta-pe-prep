# Dynamic Programming

# Memoization: cache results that have already been calculated

# Example: Without memoization
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    return result

# With memoization:
def fib(n, memo):
    # If we've already calculated this result, return it
    if memo[n] is not None:
        return memo[n]
    
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = result
    return result

num = 100
memo =  [None] * (num + 1)
print(fib(num, memo))