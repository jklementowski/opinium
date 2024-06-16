def reverse_string(s: str) -> str:
    return s[::-1]

print(reverse_string("zatrudnijcie mnie nie pozalujecie"))



import pytest 
from test_decorators import get_test_suite

def test_suite1(func):
    func.suite = 'test_suite1'
    return func

@test_suite1
def test_pytestowy():
    assert 1 == 1

'''
requirments.txt
    pytest 
    requests
    responses
    pytest-html
    

CICD

name: cicd

on: [push]

jobs:
    build:
        runs-on: ubuntu-latest
    steps:
    - name: req
      run: |
     python -m pip install --upgrade pip
     pip install -r requirments.txt
    

'''

