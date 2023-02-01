from flask import Flask
from cryptography.fernet import Fernet
import requests
import base64

url = base64.b64encode(b'http://127.0.0.1:5000/          ')
SECRET_KEY = url
SECRET_MESSAGE = b'fluffy tail'
app = Flask(__name__)

my_cipher = Fernet(SECRET_KEY)

@app.route("/")
def get_secret_message():
    return my_cipher.encrypt(SECRET_MESSAGE)

if __name__ == "__main__":
    app.debug = True
    app.run()