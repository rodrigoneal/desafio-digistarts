import requests
from random import randint


def test_app_is_alive():
    response = requests.get('http://127.0.0.1:5000/')
    assert response.status_code == 200


def test_status_code_404_not_defined_limit():
    response = requests.post('http://127.0.0.1:5000/limit/')
    assert response.status_code == 404


def test_status_code_201_defined_limit():
    response = requests.post('http://127.0.0.1:5000/limit/4')
    assert response.status_code == 201


def test_return_json_post_passed_value_number():
    numero = randint(-1000, 1000)
    response = requests.post('http://127.0.0.1:5000/', json={"number": numero})
    assert response.json() == {'id': 0, 'number': numero}


def test_status_code_200_put_passed_id():
    response = requests.put('http://127.0.0.1:5000/id/0', json={"number": 8})
    assert response.status_code == 200


def test_return_json_value_change_with_put():
    post = requests.post('http://127.0.0.1:5000/', json={"number": 15})
    assert post.json() == {'id': 1, 'number': 15}
    requests.put('http://127.0.0.1:5000/id/1', json={"number": 10})
    response = requests.get('http://127.0.0.1:5000/id/1')
    assert response.json() == {'id': 1, 'number': 10}
