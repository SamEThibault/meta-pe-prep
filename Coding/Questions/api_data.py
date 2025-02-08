"""
Read data from an API call that gives structured data in JSON format and idk make it look good or smt
"""

import requests

def get_data(url):
    res = requests.get(url, timeout=5).json()

    print(res.keys())
    userId = res['userId']
    id = res['id']
    title = res['title']
    completed = res['completed']

    print("some nice format...")


get_data('https://jsonplaceholder.typicode.com/todos/1')