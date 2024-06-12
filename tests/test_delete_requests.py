import requests
from test_decorators import delete_test_suite

@delete_test_suite
def test_delete_post():
    post_id = 1 
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    response = requests.delete(url)

    assert response.status_code == 200