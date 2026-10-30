def caesar_cipher(text, shift):
    result = ""
    # Loop through every character, if it's a letter, cipher it, if not, leave it as is.
    i = 0
    for character in text:
        if text[i].isupper:
            ascii_char_after_cipher = ord(text[i]) + shift
            char_after_cipher = chr(ascii_char_after_cipher)
            result = result + char_after_cipher
        elif text[i].islower:
            ascii_char_after_cipher = ord(text[i]) + shift
            char_after_cipher = chr(ascii_char_after_cipher)
            result = result + char_after_cipher
        else:
            result = result + text[i]
        i += 1
    return result

def caesar_decipher(text, shift):
    result = ""
    # Loop through every character, if it's a letter, decipher it, if not, leave it as is.
    j = 0
    for character in text:
        if text[j].isupper:
            ascii_char_after_decipher = ord(text[j]) - shift
            char_after_decipher = chr(ascii_char_after_decipher)
            result = result + char_after_decipher
        elif text[j].islower:
            ascii_char_after_decipher = ord(text[j]) - shift
            char_after_decipher = chr(ascii_char_after_decipher)
            result = result + char_after_decipher
        else:
            result = result + text[j]
        j += 1
    return result



# Main program
if __name__ == "__main__":
    shift = 3 # The fixed number of positions to shift

    # Read the plaintext from input.txt
    with open("input.txt", "r") as file:
        plaintext = file.read()

    # Apply the Caesar cipher for encryption
    encrypted_text = caesar_cipher(plaintext, shift)
    print("Encrypted Text:\n", encrypted_text)

    # Write the encrypted text to encrypted.txt
    with open("encrypted.txt", "w") as file:
        file.write(encrypted_text)

    # Decrypt the encrypted text
    decrypted_text = caesar_decipher(encrypted_text, shift)
    print("\nDecrypted Text:\n", decrypted_text)

    # Write the decrypted text to decrypted.txt
    with open("decrypted.txt", "w") as file:
        file.write(decrypted_text)
