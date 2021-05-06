import os
import glob

import xml.etree.ElementTree as ET

def recuperer_tout_documents():
    """Récupère la liste de tout les documents xml présents dans l'arborescence

    Returns:
        List[string]: La liste des fichiers qui ont été trouvés.
    """
    liste_fichiers = glob.glob('./**/*.xml', recursive=True)

    liste_documents = []
    for document in liste_fichiers:
        arbre_document = ET.parse(document)
        root = arbre_document.getroot()
        liste_documents.append({'titre': root.find('.//TITRE').text, 'id': root.find('.//ID').text})
    return liste_documents