# Hash-Cracker
Python Hash Cracker Code (Utilises dictionary attack)

Hash cracking is the process of recovering a plaintext from a given hash value.

This Python code allows a user to enter a hash value to crack, and reads through the dictionary.txt file, finding a password that matches the hash. The code uses the hashlib to convert each password in the dictionary to a hash value, comparing it to the input hash value. 

If a matching hash is found, the password is printed out into the console. Else, the code prints a message saying "Password not found in dictionary"


Weak passwords in dictionary.txt are samples produced by AI.
