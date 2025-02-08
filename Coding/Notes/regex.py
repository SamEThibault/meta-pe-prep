# Regex

# Basic syntax:
# - Literals: match the exact characters: "hello" matches "hello"
# - Metacharacters: special characters for defining patterns:
#   - . : matches any single character except a newline
#   - ^ : matches the start of a string
#   - $ : matches the end of a string
#   - * : matches 0 or more occurrences of the preceding character
#   - + : matches 1 or more occurrences of the preceding character
#   - ? : matches 0 or 1 occurrences of the preceding character
#   - {n,m} : matches between n and m occurrences
# - Character sets:
#   - [abc] : matches any of a b or c
#   - [^abc] : matches anything except a b or c
#   - [a-z] : matches any lowercase letter
#   - [0-9] : matches any digit
# - Escape Sequences:
#   - \d : matches any digit
#   - \D : matches any non-digit
#   - \w : matches word characters
#   - \W : matches any non-word characters
#   - \s : matches whitespace
#   - \S : matches non-whitespace
# - Alteration: a|b matches a or b

import re

re.match(pattern, string) # matches pattern at the start of the string
re.search(pattern, string) # searches for the first occurrence of the pattern anywhere in the string
re.findall(pattern, string) # returns a list of all matches
re.finditer(pattern, string) # returns an iterator yielding match objects
re.sub(pattern, replacement, string) # replaces all occurrences of the pattern with replacement
re.split(pattern, string) # splits the string at each match of the pattern

# Example: email validation
email = "user@example.com"
pattern = r"^[\w.%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$"
if re.match(pattern, email):
    print("Valid email")

# Example: extract specific parts of a date
text = "Today's date is 2025-01-24."
pattern = r"(\d{4})-(\d{2})-(\d{2})"
match = re.search(pattern, text)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")