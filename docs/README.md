# Testing Scenarios for JSONPlaceholder API 
--
## Introduction
** This project is an API Testing and Mocking Framework built using Python. It is designed to test the JSONPlaceholder API, a fake online REST API for testing. The framework supports various testing scenarios including GET, POST, PUT, PATCH, and DELETE requests, along with the ability to mock API responses for comprehensive testing. **
--
## Technologies Used
- Python 3.9
- requests for HTTP requests
- pytest for writing and running tests
- responses for mocking HTTP responses
- GitHub Actions for CI 
- pytest-html for generating test reports
--
## Test Scenarios
- GET Requests:
+ Fetch all posts.
+ Fetch a specific post by ID.
+ Fetch all comments for specific post.
- POST Requests:
+ Create a new post with a JSON payload.
- PUT/PATCH Requests:
+ Update a specific post.
- DELETE Requests:
+ Delete a specific post.
Mocking Responses:
+ Simulate server errors.
+ Test for timeout scenarios.