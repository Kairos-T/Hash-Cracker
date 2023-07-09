import hashlib
import bcrypt
import os
import threading

hash_to_crack = input("Enter the hash to crack: ").strip().lower()
dictionary_path = input("Enter the path to the dictionary file: ")
hash_algorithm = input("Enter the hash algorithm (bcrypt, sha256, md5): ").strip().lower()

if not os.path.exists(dictionary_path) or not os.path.isfile(dictionary_path):
    print("Invalid dictionary file path.")
    exit()
    
def crack_hash(password, algorithm):
    if algorithm == "bcrypt":
        salt = bcrypt.gensalt()
        hash_value = bcrypt.hashpw(password.encode(), salt).decode()
    elif algorithm == "sha256":
        hash_value = hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == "md5":
        hash_value = hashlib.md5(password.encode()).hexdigest()
    else:
        print("Invalid hash algorithm.")
        return

    if hash_value == hash_to_crack:
        print(f"Password found: {password}")
        os._exit(0)  # Terminate other threads when a match is found

with open(dictionary_path, "r") as f:
    threads = []
    for line in f:
        password = line.strip().lower()
        t = threading.Thread(target=crack_hash, args=(password, hash_algorithm))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Password not found in the dictionary")
