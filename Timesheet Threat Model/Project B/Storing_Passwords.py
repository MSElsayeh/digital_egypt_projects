from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import os, sys

# Function to find the path of a given file
def findPath(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    return file_path

# Function to check if a file exists
def checkExistence(filename):
    path = findPath(filename)
    file_exists = os.path.isfile(path)
    return file_exists


# Checking if the user already has a master key
if checkExistence("master_key.txt") is False:
    print("Create your master key to begin.")
    sys.exit()

# User input
domain = input("Enter the domain of the website: ")
username = input("Enter the username of that website: ")
password = input("Enter the password of that website: ")

# Encoding the password, then encrypting via Fernet
password_in_bytes = password.encode()
key = Fernet.generate_key()
cipher_suite = Fernet(key)
encrypted_password = cipher_suite.encrypt(password_in_bytes)

# Create the hash for the encrypted password
digest = hashes.Hash(hashes.SHA256())
digest.update(encrypted_password)
password_hash = digest.finalize().hex()

# Store the credentials in a file, making a newline for each entry
f = open(findPath("credentials.txt"), "a")
f.write("\n" + domain + ":" + username + ":" + key.decode() + ":" + encrypted_password.decode() + ":" + password_hash)
f.close()