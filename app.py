from flask import Flask, abort

import json
import re

import flaskapi.services.document_service as docs

api = Flask(__name__)

@api.route('/docs', methods=['GET'])
def recuperer_liste_documents():
    return json.dumps(docs.recuperer_tout_documents())

@api.route('/docs/<id_document>', methods=['GET'])
def recuperer_document_par_id(id_document):

    if not re.match("JURITEXT[0-9]+", str(id_document)):
        abort(404)

    document = docs.recuperer_document_par_id(id_document)

    if document is None:
        abort(404)
        
    return json.dumps(document)