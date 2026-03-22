import argparse
import glob

print("Bonjour je suis l'analyseur de LOGS")

analyseur = argparse.ArgumentParser(description="Analyse des fichiers de logs")
analyseur.add_argument("--source")

analyseur.add_argument("--niveau", default="ALL")

args = analyseur.parse_args()

# print("Le dossier a analyser est :", args.source, " au niveau :" ,args.niveau ,required=True)

print("Dossier : ", args.source)
print("Niveau : ", args.niveau)