from marshmallow import Schema, fields, ValidationError

class PokemonFavoriteSchema(Schema):
    pokemon_id = fields.Str(
        #requerimientos a validar
        required= True,
        validate= lambda x: len(x) > 0,
        error_messages={
            "required": "El nombre es requerido"
        }
    )
