from flask import Flask
api = Flask(__name__)

@api.route('/')
def hello_world():
    return 'Hello World!'

@api.route('/docs', methods=['GET'])
def recuperer_liste_documents():
    return 