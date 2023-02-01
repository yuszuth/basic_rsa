from cryptography.fernet import Fernet
import requests
import base64

url = base64.b64encode(b'http://127.0.0.1:5000/          ')
SECRET_KEY = url
my_cipher = Fernet(SECRET_KEY)

def get_secret_message():
    response = requests.get("http://127.0.0.1:5000/")
    decrypted_message = my_cipher.decrypt(response.content)
    print(f"The codeword is: {decrypted_message.decode()}")

if __name__ == "__main__":
    get_secret_message()