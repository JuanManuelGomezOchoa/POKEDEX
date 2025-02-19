from flask import Blueprint, jsonify 
from app.models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemon", __name__, url_prefix="/pokemon")
pokemon_model = ModelFactory.getModel("pokemons")

@bp.route("/get_pokemons/", methods=["GET"])
def get_pokemon():
    pokemon = pokemon_model.find_all()
    return jsonify(pokemon, 200)

@bp.route("/get_pokemon/<string:pokemon_id>", methods=["GET"])
def get_user(pokemon_id):
    pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
    return jsonify(pokemon, 200)