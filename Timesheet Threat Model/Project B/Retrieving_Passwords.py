from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import os, time, sys

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

# Function to retreive the entries in "credentials.txt"
def retrieveCredentials():
    # Search for the entry
    domain_to_be_searched = input("Write the domain of the website you're looking for: ")
    f = open(findPath("credentials.txt"), "r")
    for line in f:
        if domain_to_be_searched in line:
            domain_credentials = line
    # Use ":" as a delimiter (to separate the entry's contents)
    domain_credentials = domain_credentials.split(":")
    # Retrieve the contents based on their index with the colon, strip() to ensure no whitespace
    username = domain_credentials[1].strip()
    key = domain_credentials[2].strip()
    encrypted_password = domain_credentials[3].strip()
    password_hash = domain_credentials[4].strip()

    # Encode the retrieved key, decrypt the password and return the credentials to the user
    key = key.encode()
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password.encode())
    print("Your username is: " + username)
    print("Your password is: " + decrypted_password.decode())

# Checking if the user already has a master key
if checkExistence("master_key.txt") is False:
    print("Create your master key to begin.")
    sys.exit()

# Ask the user for the master key
master_key_input = input("Enter your Master Key: ")
master_key_input = master_key_input.encode()

# Get the hash and the salt from the master_key file
f = open(findPath("master_key.txt"), "r")
content = f.read()
split_content = content.split(":")
salt = ':'.join(split_content[1:]).strip()
actual_hash = split_content[0].strip()
f.close()

# Calculate a hash using the user input and the salt
digest = hashes.Hash(hashes.SHA256())
digest.update(master_key_input + salt.encode())
hash = digest.finalize().hex()

# Check whether or not the two hashes match
if hash == actual_hash:
    retrieveCredentials()
    response = input("Would you like to find anything else? (yes/no) ")
    if response == "yes":
        print("Timeout for 10 seconds.")
        time.sleep(10)
        retrieveCredentials()
    elif response == "no":
    	print("Exiting...")
    else:
        response = input("Invalid Response. Use yes or no.")

else:
    print("Incorrect master key. Try again.")




