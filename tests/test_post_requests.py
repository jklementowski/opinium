import requests

def test_create_new_post():
    url = 'https://jsonplaceholder.typicode.com/posts'
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response =  requests.post(url,json=payload, headers=headers)

    assert response.status_code == 201
    created_post = response.json()
    assert created_post['title'] == payload['title']
    assert created_post['body'] == payload['body']
    assert created_post['userId'] == payload['userId']