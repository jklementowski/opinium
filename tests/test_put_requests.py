import requests

def test_update_post():
    post_id = 1 
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    payload = {
        "id": post_id,
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.put(url,json=payload,headers=headers)

    assert response.status_code == 200
    updated_post = response.json()
    assert updated_post['title'] == payload['title']
    assert updated_post['body'] == payload['body']
    assert updated_post['userId'] == payload['userId']
    
