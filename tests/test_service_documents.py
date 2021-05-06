import flaskapi.services.document_service as docs
import re

def test_recuperation_tout_documents():
    liste_documents = docs.recuperer_tout_documents()
    assert len(liste_documents) == 34
    for fichier in liste_documents:
        assert re.match("[A-Z]+[0-9]+", fichier['id'])