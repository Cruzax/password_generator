import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    try:
        length = int(input("Longueur du mot de passe : "))
        print("Mot de passe généré :", generate_password(length))
    except ValueError:
        print("Entrez un nombre valide.")
