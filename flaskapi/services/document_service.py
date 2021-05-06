import os
import glob

import xml.etree.ElementTree as ET

def recuperer_tout_documents():
    """Récupère la liste de tout les documents xml présents dans l'arborescence

    Returns:
        List[Dict[{titre: string, id: string}]]: La liste des fichiers qui ont été trouvés.
    """
    liste_fichiers = glob.glob('./**/*.xml', recursive=True)

    liste_documents = []
    for document in liste_fichiers:
        arbre_document = ET.parse(document)
        root = arbre_document.getroot()
        liste_documents.append({'titre': root.find('.//TITRE').text, 'id': root.find('.//ID').text})
    return liste_documents

def recuperer_document_par_id(id_document):
    """Récupère les documents correspondants à l'ID indiqué. si aucun n'a été trouvé, on lance une erreur 404.

    Args:
        id_document (string): l'id du document tel qu'il est dans le nom et à l'intérieur du document.

    Returns:
        Dict[{titre: string, id: string, contenu: string}]
    """
    liste_fichiers = glob.glob('./**/'+id_document+'.xml', recursive=True)

    if len(liste_fichiers) != 1:
        return None

    document=liste_fichiers[0]
    arbre_document = ET.parse(document)
    root = arbre_document.getroot()
    return {
        'titre': root.find('.//TITRE').text,
        'id': root.find('.//ID').text,
        'contenu': extraire_contenu_du_document(root)
    }

def extraire_contenu_du_document(root):
    """Utilitaire permettant d'extraire le contenu du document dans une string.

    Args:
        root (Element): la racine du document XML

    Returns:
        [str]: le contenu du document
    """
    contenu = ''
    for element in root.findall('.//BLOC_TEXTUEL/CONTENU'):
        contenu = contenu.join(element.itertext())
    return contenu