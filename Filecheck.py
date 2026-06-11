import base64
import hashlib
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
from pyfiglet import Figlet



# setting defualt path
PATH = os.path.expanduser("~/Desktop/testfolder")

def banner(txt):
    f = Figlet(font='banner')
    print(f.renderText(txt))

def decrypt(file):

    with open(file, "rb") as f:
        data = f.read()

    salt = data[:16]
    encryptdata = data[16:]

    passphrase = input("Enter passphrase for this DB : ")

    kdf = Argon2id(
        salt=salt,
        length=32,
        iterations=1,
        lanes=4,
        memory_cost=64 * 1024,
        ad=None,
        secret=None,
    )

    key = base64.urlsafe_b64encode(
        kdf.derive(passphrase.encode("utf-8"))
    )

    fernet = Fernet(key)

    try:
        decrypted_data = fernet.decrypt(encryptdata)
        with open(file, "wb") as f:
            f.write(decrypted_data)

        print("Decryption successful.")
        return True

    except Exception:
        print("Incorrect passphrase or corrupted file.")
        return False




def checksumfile() :
    banner("Checking File intengrity")

    #input the name of the file(in PATH)
    file = input("pick a file to check")

    with open(PATH +'/'+file, "rb") as current_file:
        filecheck = hashlib.sha256(current_file.read()).hexdigest()

    with open("hashDB.txt","r") as f:
         data = f.read()
         for d in data.splitlines():
            filename, filehash = d.strip().split(":", 1)
            if filename == file.split("/")[-1]:
                if filehash == filecheck:
                    print(f"file {filename} is valid")
                else:
                    print(f"file {filename} has been changed")
                break
            else:
                 print("file not found")







