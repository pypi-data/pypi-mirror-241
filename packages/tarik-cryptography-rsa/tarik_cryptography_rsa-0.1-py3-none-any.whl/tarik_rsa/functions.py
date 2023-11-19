from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import serialization,hashes
import os

key_folder = ".keys"
encrypt_folder = ".encrypt"
nbits = 2048

def welcome():
    create_folders()
    print("=========================== BIENVENU ===========================")
    print("=========================== CHIFFREMENT ET DECHIFFREMENT RSA ===========================")
    print("On tiendra compte du fait que la clé est générée sur 2048 bits.")
    print("Pour le chiffrement comme le déchiffrement la fonction de hachage utilisée est le SHA256.")
    print("On limitera le test à la saisie d'un message à chiffrer")
    print("Ici on prendra 3 utilisateurs pour simuler le chiffrement et le déchiffrement.")

def createUsers():
    print("=========================== CREATION D'UTILISATEUR ===========================")
    users = {}
    id = 0
    while id < 3 :
        name = input("Entrez un nom d'utilisateur : ")
        if name in users :
            print("Ce nom d'utilisateur existe déjà !")
            continue
        password  = input("Entrez votre mot de passe : ")

        rsa_key_file_name = generate_rsa_key(nbits, id)

        users[name] = {
            "password": password,
            "public_key": generate_public_key(rsa_key_file_name),
            "private_key": rsa_key_file_name
        }
        id += 1
    return users

def connection(users):
    error = True

    print("=========================== CONNEXION ===========================")
        
    while(error):

        name = input("Nom d'utilisateur : ")
        password = input("Mot de passe : ")

        try:
            users[name]
            error = False

            if password == users[name]["password"]:
                print("Connexion autorisée !")

        except:
            error = True
            print("Ce nom d'utilisateur n'existe pas")
    return name

def disconnect(username):
    question = ""
    while (question != "O") and (question != "N"):
        question = input("voulez-vous déconnectez ? (O/N)")

        if (question != "O") and (question != "N"):
            print("Veuillez saisir soit O ou N")
    
    if question == "O":
        return None
    else:
        return username
    
def shutdown():
    question = ""
    while (question != "O") and (question != "N"):
        question = input("voulez-vous terminez le programme ? (O/N)")

        if (question != "O") and (question != "N"):
            print("Veuillez saisir soit O ou N")
    
    if question == "O":
        return False
    else:
        return True

def choice():

    print("============================= CHOIX =============================")
    print("1. Chiffrer un message")
    print("2. Déchiffrer un message")
    print("=========================== FIN CHOIX ===========================")

    choice = 0

    while choice <= 0 or choice > 2 :
        try:
            choice = int(input("Veuillez choisir : "))

            if choice <= 0 or choice > 2 :
                print("Nombre entier entre 1 et 2 (inclus)")
        except:
            print("Veuillez saisir un nombre entier !")
    return choice

def choice_user(users, username):
    keys_in_list = list(users.keys())
    if username in users :
        keys_in_list.remove(username)
    users_key_length = len(keys_in_list)

    print("============================= CHOIX =============================")
    for i in range(0,users_key_length):
        print(f"{i+1}. {keys_in_list[i]}")
    print("=========================== FIN CHOIX ===========================")

    choice = 0

    while choice <= 0 or choice > users_key_length :
        try:
            choice = int(input("Veuillez choisir : "))

            if choice <= 0 or choice > users_key_length :
                print(f"Nombre entier entre 1 et {users_key_length} (inclus)")
        except:
            print("Veuillez saisir un nombre entier !")
    return users[keys_in_list[choice - 1]]["public_key"]

def get_private_key_from_username(users, username):
    return users[username]['private_key']

def do_with_choice(choice, users, username):
    if choice == 1:
        chosen_user_public_key = choice_user(users, username)
        message = input("Veuillez saisir le message à envoyer : ")
        message = message.encode('utf-8')
        encrypt_message(message, chosen_user_public_key)
    else:
        files = os.listdir(encrypt_folder)
        print("=========================== LISTE DES FICHIERS CHIFFRES ===========================")
        if(len(files) == 0):
            print("Aucun fichier à déchiffrer")
            print("=========================== FIN LISTE ===========================")
        else :
            chosen_file = ""
            for file in files:
                print(file)
            
            print("=========================== FIN LISTE ===========================")
            
            while chosen_file not in files : 
                chosen_file = input("Choisissez un fichier : ")
                if chosen_file not in files:
                    print("Le fichier n'existe pas")
            decrypt_message(chosen_file, get_private_key_from_username(users, username))

def create_folders():
    if not os.path.exists(key_folder):
        os.mkdir(key_folder)    
    if not os.path.exists(encrypt_folder):
        os.mkdir(encrypt_folder)    

def generate_rsa_key (nbits, id):

    generated_rsa_key = rsa.generate_private_key(
        public_exponent = 65537,
        key_size = nbits
    )

    file_name = f"key_{id+1}.pem"
    pem = get_private_key(generated_rsa_key)

    with open(f"{key_folder}/{file_name}",'wb') as file:
        file.write(pem)
    
    return file_name

def generate_public_key(file_key_name):
    full_path = f"{key_folder}/{file_key_name}"
    file_name = f"{file_key_name.split('.')[0]}_public.pem"
    if os.path.exists(full_path):
        with open(full_path,'rb') as file:
            rsa_key = serialization.load_pem_private_key(
                file.read(),
                password=None,
            )
            pem = get_public_key(rsa_key)
            with open(f"{key_folder}/{file_name}",'wb') as file_2:
                file_2.write(pem)
        return file_name

def get_public_key(rsa_key):
    return rsa_key.public_key().public_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PublicFormat.SubjectPublicKeyInfo
    )

def get_private_key(rsa_key):
    return rsa_key.private_bytes(
        encoding = serialization.Encoding.PEM,
        format = serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm = serialization.NoEncryption()
    )

def encrypt_message(message, receiver_public_key_file_name):
    full_path = f"{key_folder}/{receiver_public_key_file_name}"

    if os.path.exists(full_path):

        with open(full_path, 'rb') as file:
            rsa_public_key = serialization.load_pem_public_key(
                file.read()
            ) 
            ciphertext = rsa_public_key.encrypt(
                message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            with open(f"{encrypt_folder}/{receiver_public_key_file_name.split('.')[0]}_encrypt", 'wb') as file_2:
                file_2.write(ciphertext)
    return f"{receiver_public_key_file_name.split('.')[0]}_encrypt"

def decrypt_message(encrypted_file_name, rsa_private_key_file_name):
    full_path_encrypt = f"{encrypt_folder}/{encrypted_file_name}"
    full_path_key = f"{key_folder}/{rsa_private_key_file_name}"

    if os.path.exists(full_path_encrypt) and os.path.exists(full_path_key):
        
        with open(full_path_key, 'rb') as file : 
            rsa_private_key = serialization.load_pem_private_key(
                file.read(),
                password=None
            )
            with open(full_path_encrypt, 'rb') as file_2:
                try:
                    plaintext = rsa_private_key.decrypt(
                        file_2.read(),
                        padding.OAEP(
                            mgf=padding.MGF1(algorithm=hashes.SHA256()),
                            algorithm=hashes.SHA256(),
                            label=None
                        )
                    )
                    print(plaintext)
                except:
                    print("Votre clé ne peut pas déchiffrer ce message !")
                    print("Ce message ne vous appartient pas !")