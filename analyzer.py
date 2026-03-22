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


total_lignes = 0

# lecture de chaque fichiers
for fichier in fichiers_log:
    # ouverture du fichier en mode lecturee seule
    with open(fichier, "r", encoding="utf-8") as f:
        lignes = f.readlines() #on lit toutes les lignes du fichier
        total_lignes = total_lignes + len(lignes) #on ajoute le nombre de lignes au total

        print(fichier, "contient", len(lignes), "lignes") #on dit ce fichier contient combien de lignes d'abord

print("Total de toutes les lignes :", total_lignes)

