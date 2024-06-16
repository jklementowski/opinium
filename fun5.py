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

class simple_class:
    """representing stack data strucuture"""
    def __init__(self):
        self.stack = []
        print("Stack is: ",self.stack)
        
    def push_stack(self,number: int):
        self.stack.append(number)
        print("Pushed ", number)
    
    def pop_stack(self) -> int:
        print("Popped last one")
        return self.stack.pop()

object_simple_class = simple_class()
object_simple_class.push_stack(1)
print("Current stack: ",object_simple_class.stack)
object_simple_class.push_stack(2)
object_simple_class.push_stack(3)
object_simple_class.push_stack(4)
print("Current stack: ",object_simple_class.stack)
object_simple_class.pop_stack()
print("Current stack: ",object_simple_class.stack)
