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

def test_recupere_tout_documents(client):
    response = client.get('/docs')
    data = json.loads(response.data)
    assert len(data) == 34
    assert data[0]['titre'] == "Cour de cassation, criminelle, Chambre criminelle, 13 mars 2018, 17-82.964, Publi\u00e9 au bulletin"
    assert data[0]['id'] == "JURITEXT000036741973"

def test_recupere_document_par_id_present(client):
    response = client.get('/docs/JURITEXT000036741973')
    data = json.loads(response.data)
    assert data['titre'] == "Cour de cassation, criminelle, Chambre criminelle, 13 mars 2018, 17-82.964, Publi\u00e9 au bulletin"
    assert data['id'] == "JURITEXT000036741973"
    assert len(data['contenu']) == 3296

def test_recupere_document_par_id_correct_mais_non_present(client):
    response = client.get('/docs/JURITEXT111')
    assert response.status == '404 NOT FOUND'

def test_recupere_document_par_id_incorrect(client):
    response = client.get('/docs/blah')
    assert response.status == '404 NOT FOUND'