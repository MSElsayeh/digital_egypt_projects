from cryptography.hazmat.primitives import hashes
import os, string

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
if checkExistence("master_key.txt"):
    print("You have already created a master key.")
else:
    # Prompt the user to create a new master key
    master_password = input("Make sure your password is more than 12 characters long, contains lowercase, uppercase, digits and special symbols.\nCreate a new master key: ")

    # Confirm Password Requirements
    contains_digits = any(char.isdigit() for char in master_password)
    contains_symbols = any(char in string.punctuation for char in master_password)
    contains_uppercase = any(char.isupper() for char in master_password)
    contains_lowercase = any(char.islower() for char in master_password)

    # Prompt the user again if the password does not meet the requirements
    while len(master_password) < 12 or not contains_digits or not contains_symbols or not contains_uppercase or not contains_lowercase:
        print("The master key does not meet the requirements. Try again.")
        master_password = input("Create a new Master Key: ")
        # Update the requirements' confirmations
        contains_digits = any(char.isdigit() for char in master_password)
        contains_symbols = any(char in string.punctuation for char in master_password)
        contains_uppercase = any(char.isupper() for char in master_password)
        contains_lowercase = any(char.islower() for char in master_password)


    # Prepare the random salt value and add it to the master password
    salt = os.urandom(16).hex()
    master_password += salt
    
    # Convert the master key to bytes, then hash it in hex format
    master_password = master_password.encode()
    digest = hashes.Hash(hashes.SHA256())
    digest.update(master_password)
    hash = digest.finalize().hex()

    # Store the hash and the salt in a separate file
    f = open(findPath("master_key.txt"), "w")
    f.write(hash + ":" + salt)
    f.close()

    print("Master key created successfully.")
    


