from cryptography.fernet import Fernet
from tkinter import filedialog as fd
# Generate a random AES key
key = Fernet.generate_key()

# Initialize the Fernet cipher with the key
cipher_suite = Fernet(key)
file_to_enc = fd.askopenfilename()

# Read the plaintext from a file
with open(file_to_enc,'rb') as plaintext_file:
    plaintext = plaintext_file.read()

# Encrypt the plaintext
encrypted_data = cipher_suite.encrypt(plaintext)

# Write the encrypted data to a file
with open('encrypted.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

# Save the encryption key to a file (keep it secret)
with open('encryption_key.txt', 'wb') as key_file:
    key_file.write(key)
