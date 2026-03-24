"""
Script de test pour archiver.py
Teste les trois fonctions principales :
- creer_dossier_backups()
- creer_archive()
- nettoyer_anciens_rapports()
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

# Import des fonctions d'archiver
from archiver import creer_dossier_backups, creer_archive, nettoyer_anciens_rapports


def creer_fichiers_test():
    """Crée des fichiers .log de test dans logs_test/"""
    dossier_test = os.path.join(os.path.dirname(__file__), "logs_test")
    os.makedirs(dossier_test, exist_ok=True)
    
    fichiers = []
    for i in range(1, 4):
        chemin = os.path.join(dossier_test, f"test_{i}.log")
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(f"[2026-03-24 10:00:00] INFO - Fichier de test {i}\n")
            f.write(f"[2026-03-24 10:01:00] WARN - Attention test {i}\n")
            f.write(f"[2026-03-24 10:02:00] ERROR - Erreur test {i}\n")
        fichiers.append(chemin)
        print(f"[OK] Fichier créé : {chemin}")
    
    return fichiers


def test_creer_dossier_backups():
    """Test 1 : Création du dossier backups/"""
    print("\n" + "="*60)
    print("TEST 1 : creer_dossier_backups()")
    print("="*60)
    
    try:
        creer_dossier_backups()
        dossier_backups = os.path.join(os.path.dirname(__file__), "backups")
        
        if os.path.exists(dossier_backups):
            print(f"[✓] SUCCÈS : Dossier créé à {dossier_backups}")
            return True
        else:
            print(f"[✗] ÉCHEC : Dossier non créé")
            return False
    except Exception as e:
        print(f"[✗] ERREUR : {e}")
        return False


def test_creer_archive(fichiers):
    """Test 2 : Création d'une archive tar.gz"""
    print("\n" + "="*60)
    print("TEST 2 : creer_archive()")
    print("="*60)
    
    try:
        dossier_dest = os.path.join(os.path.dirname(__file__), "backups")
        chemin_archive = creer_archive(fichiers, dossier_dest)
        
        if chemin_archive and os.path.exists(chemin_archive):
            taille = os.path.getsize(chemin_archive)
            print(f"[✓] SUCCÈS : Archive créée")
            print(f"    Chemin : {chemin_archive}")
            print(f"    Taille : {taille} bytes")
            return True
        else:
            print(f"[✗] ÉCHEC : Archive non créée ou non trouvée")
            return False
    except Exception as e:
        print(f"[✗] ERREUR : {e}")
        return False


def test_nettoyer_anciens_rapports():
    """Test 3 : Nettoyage des rapports"""
    print("\n" + "="*60)
    print("TEST 3 : nettoyer_anciens_rapports()")
    print("="*60)
    
    try:
        # Utilise une rétention très courte (0 jours) pour forcer le test
        print("[INFO] Nettoyage avec rétention = 0 jours (supprime tout)")
        nettoyer_anciens_rapports(retention_jours=0)
        print("[✓] SUCCÈS : Fonction exécutée sans erreur")
        return True
    except Exception as e:
        print(f"[✗] ERREUR : {e}")
        return False


def test_archive_vide():
    """Test 4 : Archivier une liste vide"""
    print("\n" + "="*60)
    print("TEST 4 : creer_archive() avec liste vide")
    print("="*60)
    
    try:
        resultat = creer_archive([], os.path.join(os.path.dirname(__file__), "backups"))
        
        if resultat is None:
            print("[✓] SUCCÈS : Fonction gère correctement la liste vide")
            return True
        else:
            print(f"[✗] ÉCHEC : Devrait retourner None, a retourné {resultat}")
            return False
    except Exception as e:
        print(f"[✗] ERREUR : {e}")
        return False


def main():
    """Lance tous les tests"""
    print("\n" + "#"*60)
    print("# TESTS DU MODULE ARCHIVER")
    print("#"*60)
    
    # Crée les fichiers de test
    fichiers = creer_fichiers_test()
    
    # Lance les tests
    resultats = {
        "Dossier backups": test_creer_dossier_backups(),
        "Archive tar.gz": test_creer_archive(fichiers),
        "Nettoyage rapports": test_nettoyer_anciens_rapports(),
        "Archive vide": test_archive_vide(),
    }
    
    # Résumé
    print("\n" + "="*60)
    print("RÉSUMÉ DES TESTS")
    print("="*60)
    
    total = len(resultats)
    passes = sum(1 for v in resultats.values() if v)
    
    for test, resultat in resultats.items():
        status = "✓ PASS" if resultat else "✗ FAIL"
        print(f"{status} : {test}")
    
    print(f"\nTotal : {passes}/{total} tests réussis")
    
    if passes == total:
        print("\n[✓] TOUS LES TESTS PASSENT ! 🎉")
        return 0
    else:
        print(f"\n[✗] {total - passes} test(s) échoué(s)")
        return 1


if __name__ == "__main__":
    sys.exit(main())
