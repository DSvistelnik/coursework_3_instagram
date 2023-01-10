from app import app

''' 
Тест на API первый
'''
def test_app(status_code=None):
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert type(response.json) == list
    assert (response.json[0].keys()) == ['content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count']

''' 
Тест на API второй 
'''

def test_app2(status_code=None):
    response = app.test_client().get('/api/posts/<int:post_id>')
    assert response.status_code == 200
    assert type(response.json) == list
    assert (response.json[0].keys()) == ['content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count']

