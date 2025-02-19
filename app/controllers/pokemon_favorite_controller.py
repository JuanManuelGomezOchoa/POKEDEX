
from flask import Blueprint, request, jsonify 
from app.schemas.pokemon_favorite_schema import PokemonFavoriteSchema
from app.models.factory import ModelFactory
from marshmallow import ValidationError
from bson import ObjectId
bp = Blueprint("pokemon_favorites", __name__, url_prefix="/pokemon_favorites")
pokemon_favorite_schema = PokemonFavoriteSchema()
pokemon_favorite_model = ModelFactory.getModel("pokemon_favorites")
@bp.route("/register_pokemon", methods=["POST"])
def register():
    try:
        data = pokemon_favorite_schema.load(request.json)
        pokemon_id= pokemon_favorite_model.create(data)
        return jsonify({"pokemon_id":str(pokemon_id)}, 200)
    
    except ValidationError as err:
        return jsonify("Los parametros enviados son correctos", 400)
    
    
@bp.route("/delete_favorite_pokemon/<string:pokemon_id>", methods=["DELETE"])
def delete(pokemon_id):
    pokemon_favorite_model.delete(ObjectId(pokemon_id))
    return jsonify("Pokemon eliminado con exito", 200)

@bp.route("/get_pokemons/", methods=["GET"])
def get_pokemon():
    pokemon = pokemon_favorite_model.find_all()
    return jsonify(pokemon, 200)