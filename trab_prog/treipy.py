from flask import Flask, json, jsonify
from flask import request
from pokemon import Treinador
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return "Backend do sistema de Pokémons: <a href=/listar_itens>API listar itens</a>"

@app.route('/listar_itens')
def listar():
    treinadores = list(map(model_to_dict, Treinador.select()))
    return jsonify({"lista": treinadores})

app.run(debug=True, port=4999)