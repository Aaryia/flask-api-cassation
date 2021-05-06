import os

import pytest
import app


@pytest.fixture
def client():
    app.api.config['TESTING'] = True

    with app.api.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert b'Hello World!' in response.data
