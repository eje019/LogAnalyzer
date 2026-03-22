import argparse
import glob

print("Bonjour je suis l'analyseur de LOGS")

analyseur = argparse.ArgumentParser(description="Analyse des fichiers de logs")
analyseur.add_argument("--source", required=True)

analyseur.add_argument("--niveau", default="ALL")

args = analyseur.parse_args()

fichiers_log = glob.glob(args.source + "/*.log")

# print(f"Le dossier a analyser est :",args.source, "au niveau :" ,args.niveau)

print("Dossier : ", args.source)
print("Niveau : ", args.niveau)
print("Fichiers trouvés :", fichiers_log)