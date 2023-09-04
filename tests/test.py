import json

def test_root(client):
    response = json.loads(client.get('/').content.decode())['status']
    expected = 'ok'
    assert response == expected