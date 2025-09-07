# analyseur.py
# Projet : Analyseur de fichiers texte
# Objectif : compter lignes, mots, et trouver les plus fréquents

from collections import Counter

# demander à l'utilisateur le chemin du fichier :
fichier = input("Entrez le chemin du fichier texte à analyser : ")

try:
    # ouverture et lecture du fichier :
    with open(fichier, "r") as f:
        contenu = f.read()
    
    # découpage en lignes :
    lignes = contenu.splitlines()
    nb_lignes = len(lignes)

    # nettoyage du texte :
    texte_nettoye = contenu
    for char in ".,!?;:()[]{}\"":
        texte_nettoye = texte_nettoye.replace(char, "")  # retirer ponctuation simple

    # découpage en mots :
    mots = texte_nettoye.split()
    nb_mots = len(mots)

    # compter les occurrences avec la classe Counter :
    compteur = Counter(mots)

    # le résultat :
    print("\n----- Résultats -----")
    print(f"Fichier analysé : {fichier}")
    print(f"Nombre de lignes : {nb_lignes}")
    print(f"Nombre de mots : {nb_mots}")

    if nb_mots > 0:
        mot_plus_frequent = compteur.most_common(1)[0]
        print(f"Mot le plus fréquent : \"{mot_plus_frequent[0]}\" ({mot_plus_frequent[1]} fois)")
        print("\nTop 5 mots :")
        for mot, freq in compteur.most_common(5):
            print(f"  - {mot} : {freq}")
    else:
        print("Aucun mot trouvé dans ce fichier.")

except FileNotFoundError:
    print("Erreur : le fichier n'existe pas !")
