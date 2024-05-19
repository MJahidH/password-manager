from  cryptography.fernet import Fernet 
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.backends import default_backend
import base64
import os 

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb")  as key_file:
        key_file.write(key) 

# write_key()
def load_key():
    file =  open("key.key","rb")
    key = file.read()
    file.close()
    return key

def write_salt():
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


master_pwd = input("Please type your mster password : ")
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
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")


while True : 
    mode = input("Would you like to add a new password or add a new password (view,add), press q to quit? ").lower()

    if mode == "q":
        break 

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue 

     





