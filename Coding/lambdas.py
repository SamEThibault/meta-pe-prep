# Lambdas

# A lambda function is a small anonymous function
# It can take any number of arguments, but can only have one expression

# Syntax: lambda arguments : expression
x = lambda a, b : a + b
x(5, 5)

# They're useful when used as anonymous functions inside another function
# Example: Sort a list of tuples by the second element:
data = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1])

# Example: Double each element in a list:
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))

# Example: Filtering a list for even numbers:
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))