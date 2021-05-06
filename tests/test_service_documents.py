import flaskapi.services.document_service as docs

def test_recuperation_tout_documents():
    liste_documents = docs.recuperer_tout_documents()
    print(liste_documents)
    assert len(liste_documents) == 34