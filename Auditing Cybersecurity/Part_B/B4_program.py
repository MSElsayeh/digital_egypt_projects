import hashlib

def calculate_md5(filename):
    # Execute the md5 function on the data.
    hash_md5 =  hashlib.md5()

    with open(filename, "rb") as file:  # Open the file in binary mode
        for chunk in iter(lambda: file.read(4096), b""):  # Read the file in chunks of 4KB
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Calculate the MD5 hash of data.txt
md5_hash = calculate_md5("data.txt")
print(f"MD5 hash of 'data.txt': {md5_hash}")
