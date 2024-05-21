from  cryptography.fernet import Fernet 
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.backends import default_backend
import base64
import os 


#  the key is used to ecrypt/decrypt passwords using Fernet encryption
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb")  as key_file:
        key_file.write(key) 


def load_key():
    file =  open("key.key","rb")
    key = file.read()
    file.close()
    return key


# the salt is used PBKDF2 derivation process to derive the encyption key to the master password
def write_salt():
# bytes string = b"hello""
# normal string = "hello"
    salt = os.urandom(16)
    with open("salt.salt","wb") as key_file:
        key_file.write(salt)

def load_salt():
    with open("salt.salt","rb") as salt_file:
        salt = salt_file.read()
        return salt 
    

    
def get_fernet(master_pwd):
    salt = load_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))
    return Fernet(key)


# write_salt()
# write_key()


master_pwd = input("Please type your master password : ")
fer = get_fernet(master_pwd)



def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data =line.rstrip()
            user,passw = data.split("|")
            print(f"User : {user} | Password : {fer.decrypt(passw.encode()).decode()}")


def add():
    name = input("Account Name : ")
    pwd = input("Password : ")

    with open("passwords.txt","a") as f:
        # encode convertes a string to bytes
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")


while True : 
    mode = input("Would you like to add a new password or view saved password (view,add,q to quit) ? ").lower()

    if mode == "q":
        break 

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue 

     





