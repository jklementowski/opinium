import requests
import responses

@responses.activate
def test_mock_get_post():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    responses.add(responses.GET,url,
                  json={"userId": 1, "id": 1, "title": "mocked title", "body": "mocked body"},
                  status=200)
    
    response = requests.get(url)
    assert response.status_code == 200
    post = response.json()
    assert post['title'] == 'mocked title'
    assert post['body'] == 'mocked body'
    