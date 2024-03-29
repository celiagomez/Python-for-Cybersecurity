from cryptography.fernet import Fernet
import os

# Generate a key and save it to a file
key = Fernet.generate_key()
with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Load the key from the file
with open('key.key', 'rb') as key_file:
    key = key_file.read()

# Create a Fernet instance with the key
fernet = Fernet(key)

# Encrypt the file (Choose your own file and replace it)
with open('Hola.txt', 'rb') as file:
    data = file.read()
encrypted_data = fernet.encrypt(data)

# Save the encrypted data to a new file
with open('Hola.txt.enc', 'wb') as file:
    file.write(encrypted_data)

# Decrypt the file
with open('Hola.txt.enc', 'rb') as file:
    encrypted_data = file.read()
decrypted_data = fernet.decrypt(encrypted_data)

# Save the decrypted data to a new file
with open('example.decrypted.txt', 'wb') as file:
    file.write(decrypted_data)