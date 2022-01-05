import os
import hashlib
import sys

BUF_SIZE = 32768
md5 = hashlib.md5()
sha256 = hashlib.sha256()


def compare_hash_windows():
    md5_file_hash = str(input("Input the original md5 hash: "))
    sha256_original_hash = str(input("Input the original sha256 hash: "))
    file_location = str(input("Type the file downloaded's location: "))
    with open (file_location, "rb")as file:
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha256.update(data)


def compare_hash_linux():
    sha256_original_hash = str(input("Input the original sha256 hash: "))
    md5_original_hash = str(input("Input the original md5 hash: "))
    file_location = str(input("Input the file location: "))
    with open(file_location,"rb") as file:
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha256.update(data)
        
        _md5 = md5.hexdigest()
        _sha256 = sha256.hexdigest()
        comparer(_md5, _sha256, md5_original_hash, sha256_original_hash)

def comparer(_md5, _sha256, md5_original_hash, sha256_original_hash):
    if _md5 == md5_original_hash and _sha256 == sha256_original_hash:
        print("File integrity is TRUE")
    else:
        print("File integrity is FALSE")        
    
    


def what_OS():
    print("A) Windows.")
    print("B) Linux.")
    UOS = input("Pick the letter of your OS: Windows or Linux: ")
    if UOS == "A":
        compare_hash_windows()
    elif UOS == "B":
        compare_hash_linux()



what_OS()