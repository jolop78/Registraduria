from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorCandidato import ControladorCandidato

app=Flask(__name__)
cors = CORS(app)

miControladorCandidato=ControladorCandidato()

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

####################CANDIDATO############################
@app.route("/candidato",methods=['GET'])
def getCandidato():
    json=miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidato",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)

@app.route("/candidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])


