import hashlib
import bcrypt
import os

hash_to_crack = input("Enter the hash to crack: ").strip().lower()
dictionary_path = input("Enter the path to the dictionary file: ")

if not os.path.exists(dictionary_path) or not os.path.isfile(dictionary_path):
    print("Invalid dictionary file path.")
    exit()

with open(dictionary_path, "r") as f:
    for line in f:
        password = line.strip().lower().encode()
        salt = bcrypt.gensalt()
        hash_value = bcrypt.hashpw(password, salt).decode()
        if hash_value == hash_to_crack:
            print(f"Password found: {password.decode()}")
            break
    else:
        print("Password not found in the dictionary")
