import pytest
import requests

def test_user_authentication(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {'username': 'admin', 'password': 'admin'}

    mocker.patch('requests.get', return_value=MockResponse(401, ''))

    response = requests.get(url, params=params)

    assert response.status_code == 401
    assert response.text == ''

def test_user_authentication_with_different_password(mocker):
    url = 'http://127.0.0.1:8000/users'
    params = {'username': 'admin', 'password': 'qwerty'}

    mocker.patch('requests.get', return_value=MockResponse(200, ''))

    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.text == ''

class MockResponse:
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text