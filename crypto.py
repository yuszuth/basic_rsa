from cryptography.fernet import Fernet

key = Fernet.generate_key()
my_cipher = Fernet(key)
ciphertext = my_cipher.encrypt(b'fluffy_tail')
print(ciphertext)