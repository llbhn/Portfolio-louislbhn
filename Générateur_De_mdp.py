# password_tool.py
import random
import string
import hashlib

def generer_mot_de_passe(longueur=12, majuscules=True, chiffres=True, symboles=True):
    """Génère un mot de passe sécurisé"""
    caracteres = string.ascii_lowercase
    if majuscules:
        caracteres += string.ascii_uppercase
    if chiffres:
        caracteres += string.digits
    if symboles:
        caracteres += string.punctuation

    return ''.join(random.choice(caracteres) for _ in range(longueur))

def evaluer_mot_de_passe(mdp):
    """Évalue la robustesse d’un mot de passe et retourne un score"""
    score = 0
    if len(mdp) >= 12:
        score += 2
    elif len(mdp) >= 8:
        score += 1

    if any(c.islower() for c in mdp): score += 1
    if any(c.isupper() for c in mdp): score += 1
    if any(c.isdigit() for c in mdp): score += 1
    if any(c in string.punctuation for c in mdp): score += 1

    if score <= 2:
        niveau = "faible"
    elif score <= 4:
        niveau = "moyen"
    else:
        niveau = "fort"
    return niveau, score

def hacher_mot_de_passe(mdp):
    """Retourne le hash SHA256 d’un mot de passe"""
    return hashlib.sha256(mdp.encode()).hexdigest()

# Programme principal
print("1 - Générer un mot de passe")
print("2 - Évaluer un mot de passe")
print("3 - Hacher un mot de passe (SHA256)")
choix = input("Choisissez une option (1/2/3) : ")

if choix == "1":
    longueur = int(input("Longueur du mot de passe : "))
    mdp = generer_mot_de_passe(longueur)
    print("Mot de passe généré :", mdp)

elif choix == "2":
    mdp = input("Entrez le mot de passe à évaluer : ")
    niveau, score = evaluer_mot_de_passe(mdp)
    print(f"Niveau de sécurité : {niveau} (score {score})")

elif choix == "3":
    mdp = input("Entrez le mot de passe à hacher : ")
    print("Hash SHA256 :", hacher_mot_de_passe(mdp))

else:
    print("Option invalide.")
