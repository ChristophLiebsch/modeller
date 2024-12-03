from flask import Flask, jsonify

assistent_backend = Flask(__name__)

@assistent_backend.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hallo Welt, hier ist der Modellierungs Assistent!"})

if __name__ == '__main__':
    assistent_backend.run(debug=True)
