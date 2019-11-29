from flask import Flask, json, jsonify
from flask import request
from pokemon import Pokemon
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return "Backend do sistema de Pokémons: <a href=/listar_itens>API listar itens</a>"

@app.route('/listar_itens')
def listar():
    pokemons = list(map(model_to_dict, Pokemon.select()))
    return jsonify({"lista": pokemons})

app.run(debug=True, port=4999)