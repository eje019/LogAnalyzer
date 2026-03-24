import argparse
import glob

print("Bonjour je suis l'analyseur de LOGS")

analyseur = argparse.ArgumentParser(description="Analyse des fichiers de logs")
analyseur.add_argument("--source", required=True)

analyseur.add_argument("--niveau", default="ALL")

args = analyseur.parse_args()

fichiers_log = glob.glob(args.source + "/*.log")

# print(f"Le dossier a analyser est :",args.source, "au niveau :" ,args.niveau)
niveau = args.niveau 

print("Dossier : ", args.source)
print("Niveau : ", niveau)
print("Fichiers trouvés :", fichiers_log)


total_lignes = 0
compte_INFO = 0
compte_WARN = 0
compte_ERROR = 0
erreurs = {} #dictionnaire pour compter chaque message d'erreur 

for fichier in fichiers_log:
    # ouverture du fichier en mode lecturee seule
    with open(fichier, "r", encoding="utf-8") as f:
        # lignes = f.readlines() #on lit toutes les lignes du fichier
        # total_lignes = total_lignes + len(lignes) #on ajoute le nombre de lignes au total
        
        
        # gestion des filtres pour les niveaux
        for ligne in f:
            total_lignes = total_lignes + 1

            # on check ce que la ligne contient 
            if "INFO" in ligne:
                compte_INFO = compte_INFO + 1
            elif "WARN" in ligne:
                compte_WARN = compte_WARN + 1
            elif "ERROR" in ligne:
                compte_ERROR = compte_ERROR + 1
                # print(fichier, "contient", len(lignes), "lignes") #on dit ce fichier contient combien de lignes d'abord

                morceaux = ligne.split() #la ligne est decoupee

                message = " ".join(morceaux[3:])
                
                if message in erreurs:
                    erreurs[message] = erreurs[message] + 1
                else:
                    erreurs[message] = 1



# Trouver le top 5 des erreurs les plus frequentes

#copie du dictionaire des erreurs pour pouvoir supprimer les erreurs au fur et à mesure sans perdre l'original
erreurs_restantes = dict(erreurs)

top5 = [] #tableau qui va contenir les 5 meilleures erreurs
# chaque element sera un tuple (message, nombre)

for i in range(5):
    if not erreurs_restantes:
        break
    
    message_max = None
    nombre_max = -1 #nombre_max à -1 car on n'a encore rien trouve
    
    for message, nombre in erreurs_restantes.items():

        # si le nombre de cette erreur est plus grand que le plus grand
        # qu'on a jusqu'ici alors c'est elle la nouvelle championne
        if nombre > nombre_max:
            nombre_max = nombre
            message_max = message
        
    # on a l'erreur avec le plus grand nombre
    # pn l'ajoute dans le tableau top5 sous forme de couple (message, nombre)
    top5.append((message_max, nombre_max))

    # on supprime cette erreur du dictionnaire pour qu'elle ne soit pas
    # reprise lors des prochains tours de la boucle
    del erreurs_restantes[message_max]

print("----Resultats----")
print("Total de toutes les lignes :", total_lignes) #on affiche le nombre total en general
# print("INFO :", compte_INFO)
# print("ERROR :", compte_ERROR)
# print("WARN :", compte_WARN)

if niveau == "ALL" or niveau == "INFO":
    print("INFO :", compte_INFO)
if niveau == "ALL" or niveau == "WARN":
    print("WARN :", compte_WARN)
if niveau == "ALL" or niveau == "ERROR":
    print("ERROR :", compte_ERROR)

# on affiche les 5 messages d'erreur les plus frequents
print("\n----Top 5 des messages derreur----")
if top5:
    for i, (message, count) in enumerate(top5, 1):
        print(f"{i}. {message} ({count} fois)")
else:
    print("Aucune erreur trouvée")
