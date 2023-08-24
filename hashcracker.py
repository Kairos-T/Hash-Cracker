import hashlib
import bcrypt
import os
import threading
from concurrent.futures import ThreadPoolExecutor

hash_to_crack = input("Enter the hash to crack: ").strip().lower()
dictionary_path = input("Enter the path to the dictionary file: ")
hash_algorithm = input("Enter the hash algorithm (bcrypt, sha256, md5): ").strip().lower()

if not os.path.exists(dictionary_path) or not os.path.isfile(dictionary_path):
    print("Invalid dictionary file path.")
    exit()

if hash_algorithm not in ["bcrypt", "sha256", "md5"]:
    print("Invalid hash algorithm.")
    exit()

def compute_hash(password, algorithm, salt):
    if algorithm == "bcrypt":
        return bcrypt.hashpw(password.encode(), salt).decode()
    elif algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()

class PasswordFound(Exception):
    pass

def crack_hash(password, algorithm, salt):
    computed_hash = compute_hash(password, algorithm, salt)
    if computed_hash == hash_to_crack:
        raise PasswordFound(password)

def worker(password):
    try:
        crack_hash(password, hash_algorithm, bcrypt.gensalt())
    except PasswordFound as e:
        print(f"Password found: {e}")
        stop_event.set()

with open(dictionary_path, "r") as f:
    stop_event = threading.Event()
    passwords = [line.strip().lower() for line in f]

    with ThreadPoolExecutor(max_workers=10) as executor:
        for password in passwords:
            if not stop_event.is_set():
                executor.submit(worker, password)

    if not stop_event.is_set():
        print("Password not found in the dictionary")
