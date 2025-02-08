# Common Methods
# Strings are immutable, each method that "modifies" the string just returns a new string
s = "hello"
s.capitalize()
s.count("h")
s.endswith("o") # returns true of false
s.find("el") # returns index where h is found, or -1

fs = "My name is {}, I'm {}"
fs.format("Sam", 22)

s.isalnum() # true if alphanumeric
s.isalpha() # true if alphabet
s.isascii() # true if all ascii characters
s.isdecimal() # true if all decimals
s.isdigit() # true if all digits
s.islower() # true if all lowercase
s.isupper() # true if all uppercase

x = ", ".join(["hello", "world"])

s.lower() # convert to lowercase
s.upper() # convert to uppercase
s.replace("h", "H", 1) # third param is number of occurences you want to replace, default is ALL 

s.split() # returns list, param is separator
s.splitlines() # splits at linebreaks and returns list
s.strip() # removes leading and trailing whitespaces

# To check for equality, can use ==, !=, <, > (lexicographical)

int("7") # convert string to int
str(7) # convert int to string

# Concatenation
# Default concatenation str1 + str2 is O(n^2) where n is num of strings
# To avoid this, use ''.join(list_of_strings), which is O(n)

