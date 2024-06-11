import requests

def test_delete_post():
    post_id = 1 
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    response = requests.delete(url)

    assert response.status_code == 200
    response = requests.get(url)
    assert response.status_code == 404 ## failed in line with docs