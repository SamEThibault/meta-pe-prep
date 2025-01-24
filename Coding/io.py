# I/O Basics

# File I/O
file = open("text.txt", "r") # r=read, w=write, a=append, b=binary, w+=read/write

with open("text.txt", "r") as file:
    content = file.read() # reads entire file as string

with open("text.txt", "r") as file:
    for line in file:
        print(line.strip()) # read line by line, stripping newline at end of each line

with open("text.txt", "r") as file:
    lines = file.readlines() # get a list of lines

with open("text.txt", "w") as file:
    file.write("hello, world\n") # overwrites file, use a to append


# User I/O
name = input("Enter your name: ")
# input is always returned as a string, make sure to convert to other types if needed (int for ex)

# Printing without new line:
print("hello" end=" ")

# Handle file exceptions:
try:
    with open("file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    return
except IOError:
    return

# Working with OS
import os

if os.path.exists("example.txt"):
    return

# remove a file:
os.remove("example.txt")

# create dir
os.mkdir("new_dir")

# list files
os.listdir('.')

# JSON and CSV handling
import json
import csv
data = {"test": 2, "field2": 5}

with open("data.json", "w") as file:
    json.dump(data, file)
    # or data = json.load(file) if reading

# Reading CSV:
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# API stuff
import requests
response = requests.get("https://google.com")
print(response.status_code)
print(response.json())

data = {"POST_DATA": 1}
response = requests.post("https://httpbin.org/post", json=data)
print(response.json())

