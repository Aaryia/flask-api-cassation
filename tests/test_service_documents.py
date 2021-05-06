import flaskapi.services.document_service as docs
import re

def test_recuperation_tout_documents():
    liste_documents = docs.recuperer_tout_documents()
    assert len(liste_documents) == 34
    for fichier in liste_documents:
        assert re.match("[A-Z]+[0-9]+", fichier['id'])

def test_recupere_document_par_id_present():
    document = docs.recuperer_document_par_id('JURITEXT000036741973')

    assert document['titre'] == "Cour de cassation, criminelle, Chambre criminelle, 13 mars 2018, 17-82.964, Publi\u00e9 au bulletin"
    assert document['id'] == "JURITEXT000036741973"
    assert len(document['contenu']) == 3296
