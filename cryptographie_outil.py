from cryptography.fernet import Fernet

# Génération d'une clé et sauvegarde dans un fichier
def generate_key(file_path):
    key = Fernet.generate_key()
    with open(file_path, 'wb') as key_file:
        key_file.write(key)
    print(f"Clé générée et sauvegardée dans {file_path}")

# Chargement de la clé depuis un fichier
def load_key(file_path):
    with open(file_path, 'rb') as key_file:
        return key_file.read()

# Chiffrement du message
def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

# Déchiffrement du message
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

# === Programme principal ===
key_file_path = "secret.txt"

# Générer une clé si nécessaire
try:
    key = load_key(key_file_path)
except FileNotFoundError:
    generate_key(key_file_path)
    key = load_key(key_file_path)

print(f"Clé utilisée : {key}")

message = input("Entrez le message à chiffrer: ")
encrypted_message = encrypt_message(message, key)
print(f"Message chiffré: {encrypted_message}")

decrypted_message = decrypt_message(encrypted_message, key)
print(f"Message déchiffré: {decrypted_message}")
