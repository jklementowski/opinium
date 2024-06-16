'''Live Coding Challenge (Python)

Write a Python script to fetch and display data from an external API (e.g., GitHub API).
Implement a simple class in Python that represents a stack data structure.'''


import requests
import json

urljson='http://jsonplaceholder.typicode.com/posts'

def GET_from_jsonplacholer(url: str):
    response_temp = requests.get(url)
    resp_json = response_temp.json()
    print(json.dumps(resp_json, indent=4, sort_keys=True))
    return resp_json

GET_from_jsonplacholer(urljson)