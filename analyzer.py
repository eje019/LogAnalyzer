import argparse
import glob

print("Bonjour je suis l'analyseur de LOGS")

analyseur = argparse.ArgumentParser(description="Analyse des fichiers de logs")
analyseur.add_argument("--source")
args = analyseur.parse_args()
analyseur.add_argument("--niveau", default="ALL")

# print("Le dossier a analyser est :", args.source, " au niveau :" ,args.niveau ,required=True)

print("Dossier : ", args.source)
print("Dossier : ", args.niveau)