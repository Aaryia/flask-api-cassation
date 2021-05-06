import os.path
import glob
import json

def recuperer_tout_documents():
    return glob.glob('./**/*.xml', recursive=True)