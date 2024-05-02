from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import base64

app = Flask(__name__)
cipher_suite = None

@app.route('/image', methods=['POST'])
def encryptImage():
    global cipher_suite
    with open('apple.png', 'rb') as f:
        image = f.read()
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_image = cipher_suite.encrypt(image)
    return jsonify({"message": base64.b64encode(encrypted_image).decode(), "key": key.decode()})

@app.route('/image', methods=['GET'])
def decryptImage():
    global cipher_suite
    data = request.get_json()
    encrypted_image = base64.b64decode(data["message"])
    key = data["key"].encode()
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_image)
    return decrypted_message

if __name__ == '__main__':
    app.run(debug=True, port=5000)
