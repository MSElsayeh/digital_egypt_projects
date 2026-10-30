import random
import string

def generate_password():
    length = random.randint(12, 30)         # Variable length for security purposes.
    password = ""                           # Set the value to empty by default until it is set later. 
    password_string = ""                    # Same as the above comment.
    for index in range(length):
        randCharacter = random.choice(string.ascii_letters + string.digits + string.punctuation) # Generate a random character, could be an uppercase/lowercase letter, a number, or a symbol.
        password_string = password_string + randCharacter # Append the character to the string.
    return password_string

# Generate a password that meets the criteria.
password = generate_password()
print(password)
