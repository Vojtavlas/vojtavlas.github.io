from cryptography.fernet import Fernet
from tkinter import filedialog as fd
import time
# Read the encryption key from the key file
print("Select a file with encryption key")
time.sleep(3)
file_enc_key = fd.askopenfilename()
with open(file_enc_key, 'rb') as key_file:
    key = key_file.read()

# Initialize the Fernet cipher with the key
cipher_suite = Fernet(key)


# Read the encrypted data from the file
print("Select an encrypted file to decrypt")
time.sleep(3)
file_to_dec = fd.askopenfilename()
with open(file_to_dec, 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt the data
decrypted_data = cipher_suite.decrypt(encrypted_data)

# Write the decrypted data to a file
with open('decrypted.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted_data)
