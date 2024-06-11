import requests

def test_get_all_posts():
    response = requests.get('http://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200
    assert isinstance(response.json(),list)
    assert len(response.json()) > 0 