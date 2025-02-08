"""
read an innate file and parse the strings to count how many times an email address is found
"""

"""
Email requirements:
- start with alphanum
- then an @
- then alphanum
- then .
- then alphanum
"""
def validate(string):
    if string[0].isalnum():
        parts = string.split("@")
        if len(parts) > 1:
            if parts[0].isalnum():
                # we can check the second half:
                second_half = parts[1].split(".")
                if len(second_half) > 1:
                    if second_half[0].isalnum() and second_half[1].isalnum():
                        return True
    return False

# assuming each line has comma-separated strings
with open("./Coding/Questions/emails.txt", "r") as file:
    lines = file.readlines() # assuming our file isn't too large and can feasibly fit in memory

    # This is not exhaustive and doesn't cover most test cases, use proper email validator for real uses
    for line in lines:
        strings = line.split(",")
        for string in strings:
            if validate(string):
                print(f"{string} is an email address")