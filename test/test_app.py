import requests

base = 'http://127.0.0.1:5000/'
limit = 'http://127.0.0.1:5000/limit/4'


def test_app_is_alive():
    response = requests.get(base)
    assert response.status_code == 200


def test_app_defined_limit():
    response = requests.post(limit)
    assert response.status_code == 201


def test_post_passed_value_number():
    response = requests.post(base, json={"number": 5})
    assert response.json() == {'id':0, 'number':5}

