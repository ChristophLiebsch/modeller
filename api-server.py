from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve

assistent_backend = Flask(__name__)
CORS(assistent_backend)

@assistent_backend.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hallo Welt, hier ist die API des Modellierungs Assistenten!"})

if __name__ == "__main__":
    serve(assistent_backend, host="0.0.0.0", port=5000)