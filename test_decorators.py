# test_decorators.py

import pytest

def get_test_suite(func):
    func.suite = 'get_test_suite'
    return func

def post_test_suite(func):
    func.suite = 'post_test_suite'
    return func

def put_test_suite(func):
    func.suite = 'put_test_suite'
    return func

def delete_test_suite(func):
    func.suite = 'delete_test_suite'
    return func

def mocking_test_suite(func):
    func.suite = 'mocking_test_suite'
    return func