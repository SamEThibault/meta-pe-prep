"""
Write an algorithm to determine whether a string is a palindrome
"""

def palindrome(string):
    # What I would usually do:
    # return string[::-1] == string

    # But since I'm assuming they want double-indexed answer
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


print(palindrome("pelelelelelep"))