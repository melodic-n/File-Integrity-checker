from Init import encryptDB, calcchecksum
from Filecheck import checksumfile, decrypt


def main():


    #first decrypt the file using the passphrase
    print("Choose an option: \n")
    print("*1 - initliaze DB \n")
    print("*2 - check a files integrity \n")
    choice = int(input())

    if choice == 1 :
        calcchecksum()
    if choice == 2 :
        decrypt("hashDB.txt")
        checksumfile()


if __name__ == "__main__":
    main()