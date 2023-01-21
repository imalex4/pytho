import hashlib


def encrypt_file(file_name):
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()

    # Open the file in read-binary mode
    with open(file_name, 'rb') as file:
        # Iterate through the file in blocks
        for block in iter(lambda: file.read(4096), b''):
            sha256.update(block)

    # Get the hexadecimal representation of the digest
    digest = sha256.hexdigest()

    # Print the digest
    print(digest)


# Encrypt the file 'example.txt'
encrypt_file('example.txt')