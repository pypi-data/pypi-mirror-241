import tkinter as tk
from tkinter import filedialog
import csv
import os

def fusionner_fichiers_csv():
    fichier1=choisir_fichier()
    if not fichier1:
        return  # L'utilisateur a annulé la sélection

    fichier2 = choisir_fichier()
    if not fichier2:
        return  # L'utilisateur a annulé la sélection

    fichier_sortie = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])

    
    if not fichier_sortie:
        return  # L'utilisateur a annulé la sélection
    
    try:
        # Ouvrir le premier fichier  en mode lecture
        with open(fichier1, mode='r') as f1:
            lecteur_csv1 = csv.reader(f1)
            lignes_fichier1 = list(lecteur_csv1)
        # Ouvrir le deuxième fichier mode lecture
        with open(fichier2, mode='r') as f2:
            lecteur_csv2 = csv.reader(f2)
            lignes_fichier2 = list(lecteur_csv2)

    except Exception as e:
        return f"Erreur lors de la lecture des fichiers : {e}"


    # Vérifier que les deux fichiers ont au moins une colonne
    if not lignes_fichier1 or not lignes_fichier2:
        return "Erreur: Les fichiers ne contiennent pas de données."

    # Vérifier si la première colonne est identique et fusionner les fichiers en conséquence
    if lignes_fichier1[0][0] == lignes_fichier2[0][0]:
        lignes_combinees = [ligne1 + ligne2[1:] for ligne1, ligne2 in zip(lignes_fichier1, lignes_fichier2)]
    else:
        lignes_combinees = [ligne1 + ligne2 for ligne1, ligne2 in zip(lignes_fichier1, lignes_fichier2)]

    # Écrire les lignes combinées dans un nouveau fichier CSV
    try:
        with open(fichier_sortie, mode='w', newline='') as fichier_sortie_csv:
            ecrivain_csv = csv.writer(fichier_sortie_csv)
            ecrivain_csv.writerows(lignes_combinees)
        return f"Les fichiers {fichier1} et {fichier2} ont été combinés avec succès dans {fichier_sortie}."

    except PermissionError:
        return "Erreur de permission d'écriture."
    except Exception as e:
        return f"Erreur lors de l'écriture du fichier de sortie : {e}"


def choisir_fichier():
    return filedialog.askopenfilename(title="Choisir un fichier CSV", filetypes=[("Fichiers CSV", "*.csv")])
