import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from pyfiglet import Figlet
import hashlib



PATH = os.path.expanduser("~/Desktop/testfolder")
files = os.listdir(PATH) # just for test I hardcoded it it should be dynamique or somethign


def banner(txt):
    f = Figlet(font='banner')
    print(f.renderText(txt))


def encryptDB(file):

    passphrase = input("Enter passphrase for this DB : ")
    salt = os.urandom(16)
    kdf = Argon2id(
        salt=salt,
        length=32,
        iterations=1,
        lanes=4,
        memory_cost=64 * 1024,
        ad=None,
        secret=None,
    )
    key = base64.urlsafe_b64encode(kdf.derive(passphrase.encode("utf_8")))
    fernet = Fernet(key)
    with open(file,"rb") as f :
         data = f.read()
    encryptdata = fernet.encrypt(data)

    with open(file,"wb") as f :
        f.write(salt+encryptdata)


def calcchecksum():
    banner("Initializing DB ")
    with open("hashDB.txt","w") as db :
        for f in files:
            with open(PATH +'/'+ f, "rb") as current_file:
                filecheck = hashlib.sha256(current_file.read()).hexdigest()
            db.write(f"{f}:{filecheck}")
            db.write("\n")
    #encrypt the file
    encryptDB("hashDB.txt")
    banner("initilized and encrypted")





