import requests

def test_get_all_posts():
    response = requests.get('http://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200
    assert isinstance(response.json(),list)
    assert len(response.json()) > 0 

def test_get_single_post():
    post_id = 1 
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 200
    post = response.json()
    assert post['id'] == post_id
    assert 'title' in post
    assert 'body' in post

def test_get_single_post_comments():
    post_id = 1 
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')
    assert response.status_code == 200
    comments = response.json()
    first_comment = comments[0]
    expected_keys = {'postId', 
                     'id',
                     'name',
                     'email',
                     'body'}
    assert expected_keys.issubset(first_comment.keys()), "Comment does not have the expected keys"

    for comment in comments:
        assert comment['postId'] == 1, f"Expected postId to be 1, got{comment['postId']}"