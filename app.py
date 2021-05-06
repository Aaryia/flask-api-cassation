from flask import Flask

import json

import flaskapi.services.document_service as docs

api = Flask(__name__)

@api.route('/')
def hello_world():
    return 'Hello World!'

@api.route('/docs', methods=['GET'])
def recuperer_liste_documents():
    return json.dumps(docs.recuperer_tout_documents())