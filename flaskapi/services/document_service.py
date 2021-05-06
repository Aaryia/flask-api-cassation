import glob

def recuperer_tout_documents():
    """Récupère la liste de tout les documents xml présents dans l'arborescence

    Returns:
        List[string]: La liste des fichiers qui ont été trouvés.
    """
    return glob.glob('./**/*.xml', recursive=True)