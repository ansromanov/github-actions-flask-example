import app as tested_app
import json

client = tested_app.app.test_client()


def test_get_hello_endpoint():
    r = client.get('/')
    assert r.get_data() == b'Hello World!'
    assert r.status_code == 200


def test_post_hello_endpoint():
    r = client.post('/')
    assert r.status_code == 405


def test_get_api_endpoint():
    r = client.get('/api')
    assert r.json == {'status': 'test'}


def test_correct_post_api_endpoint():
    r = client.post('/api',
                    content_type='application/json',
                    data=json.dumps({'name': 'Den', 'age': 100}))
    assert r.json == {'status': 'OK'}
    assert r.status_code == 200

    r = client.post('/api',
                    content_type='application/json',
                    data=json.dumps({'name': 'Den'}))
    assert r.json == {'status': 'OK'}
    assert r.status_code == 200


def test_not_dict_post_api_endpoint():
    r = client.post('/api',
                    content_type='application/json',
                    data=json.dumps([{'name': 'Den'}]))
    assert r.json == {'status': 'bad input'}
    assert r.status_code == 400


def test_no_name_post_api_endpoint():
    r = client.post('/api',
                    content_type='application/json',
                    data=json.dumps({'age': 100}))
    assert r.json == {'status': 'bad input'}
    assert r.status_code == 400


def test_bad_age_post_api_endpoint():
    r = client.post('/api',
                    content_type='application/json',
                    data=json.dumps({'name': 'Den', 'age': '100'}))
    assert r.json == {'status': 'bad input'}
    assert r.status_code == 400
