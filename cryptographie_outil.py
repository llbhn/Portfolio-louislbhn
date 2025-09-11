from cryptography.fernet import Fernet

# Générer une clé et l'enregistrer dans un fichier
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Charger la clé
with open("secret.key", "rb") as key_file:
    key = key_file.read()

f = Fernet(key)

# Texte à chiffrer
message = input("Entrez un message à chiffrer : ").encode()

# Chiffrement
token = f.encrypt(message)
print("Message chiffré :", token)

# Déchiffrement
decrypted = f.decrypt(token)
print("Message déchiffré :", decrypted.decode())

# Afficher la clé utilisée
print("Clé utilisée (base64) :", key.decode())