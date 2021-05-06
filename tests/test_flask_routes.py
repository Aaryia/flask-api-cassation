import os

import pytest
import json

import app


@pytest.fixture
def client():
    app.api.config['TESTING'] = True

    with app.api.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert b'Hello World!' in response.data

def test_hello_world(client):
    response = client.get('/docs')
    data = json.loads(response.data)
    assert len(data) == 34
