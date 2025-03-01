from flask import Blueprint, request, jsonify #secciona el servidor en urls
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required



bp = Blueprint("pokemons",__name__, url_prefix="/pokemons")#Carpeta u endpoint
RM= ResponseManager()

pokemons= ModelFactory.get_model("pokemons")

@bp.route("/getAll", methods=["GET"])
@jwt_required()
def get_ALL():
    pokemons_all= pokemons.find_all()
    return RM.succes(pokemons_all)


@bp.route("/get/<string:pokemon_id>", methods=["GET"])
@jwt_required()
def get_pokemon(pokemon_id):
    pokemon= pokemons.find_by_id(ObjectId(pokemon_id))
    return RM.succes(pokemon)