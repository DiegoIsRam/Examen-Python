from flask import Flask, jsonify
from clientes import clientes

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})


@app.route('/clientes')
def getClientes():
    return jsonify(clientes)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
