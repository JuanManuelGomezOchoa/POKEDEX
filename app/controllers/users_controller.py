from flask import Blueprint, request #secciona el servidor en urls
from app.schemas.user_schema import UserSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app.tools.encription_manager import EncriptionManager

RM= ResponseManager()
EM= EncriptionManager()
bp = Blueprint("users",__name__, url_prefix="/users")#Carpeta u endpoint
#dice que todo lo que tenga el prefihjo users va a venir aqui
user_schema= UserSchema()
user_model = ModelFactory.get_model("users") #mandamos a traer el modelo

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email= data.get("email", None) #Pedimos un parametro, si no existe devuekve un None
    password= data.get("password", None)

    if not email or not password:
        return RM.error("Es necesario enviar todas las credenciales")
    
    user= user_model.get_by_email_password(email, password)

    if not user: 
        return RM.error("No se encontro un usario")
    if not EM.compare_hashes(password,user["password"]):
        return RM.error("Credenciales invalidas")
    return RM.succes({"user":user, "token":create_access_token(user["_id"])})

#REGISTRAR USUARIO
@bp.route("/register", methods=["POST"])
def register():
    try:
        data = user_schema.load(request.json)#Mandamos a evaluar los dtos
        data["password"]=EM.create_hash(data["password"])
        user_id=user_model.create(data) #Creamos el usuario, regres aun OBJ ID
        return RM.succes({"user_id":str(user_id),"token":create_access_token(str(user_id))}) #Mandamos respuesta json con el obj ide en texto

    except ValidationError as err:
        return RM.error("Los parametros enviados son incorrectos")

#endpoint para actualizar. Mandamos un id por la ruta
@bp.route("/update", methods=["PUT"])
@jwt_required()
def update():
    user_id=get_jwt_identity()
    try:
        data= user_schema.load(request.json)
        user= user_model.update(ObjectId(user_id), data)
        return RM.succes({
            "data": user
        })


    except ValidationError as err:
        return RM.error("Los parametros enviados son incorrectos")
    
@bp.route("/delete", methods=["DELETE"])
@jwt_required()
def delete():
    user_id=get_jwt_identity()
    user_model.delete(ObjectId(user_id))
    return RM.succes("Usuario eliminado con exito")


@bp.route("/get", methods=["GET"])
@jwt_required()
def get_user():
    user_id=get_jwt_identity()
    user= user_model.find_by_id(ObjectId(user_id))
    return RM.succes(user)