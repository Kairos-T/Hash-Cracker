import hashlib

hash_to_crack = input("Enter the hash to crack: ")
with open("dictionary.txt", "r") as f:
    for line in f.readlines():
        password = line.strip()
        hash_value = hashlib.sha256(password.encode()).hexdigest()
        if hash_value == hash_to_crack:
            print(f"Password found: {password}")
            break
    else:
        print("Password not found in the dictionary")