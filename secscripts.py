import bcrypt, os, base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def checkpw(password, hashedpassword):
    if bcrypt.checkpw(password.encode(),hashedpassword.encode()):
        print('Password accepted, welcome to the chatbot')
        return True
    else:
        print("The given password does not matches the saved password")
        if input("Do you want to try again? (y/n)") == "y":
            password = input('Password:')
            if bcrypt.checkpw(password.encode(), hashedpassword.encode()):
                print('Password accepted, welcome to the chatbot')
                return True
            else:
                print("Second fail, goodbye")
                exit()
        else:
            return False
def hashpw(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def genkey(password=None):
    if password:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'salt',
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key
    else:
        key = Fernet.generate_key()
        return key
def encrypt(key, rawtext):
    f = Fernet(key)
    encrypted = f.encrypt(rawtext.encode())
    return encrypted.decode()

def decrypt(key, encrypted):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted.encode())
    return decrypted.decode()
