from marshmallow import Schema, fields, ValidationError

class PokemonFavoriteSchema(Schema):
    pokemonName = fields.Str (
        required = True,
        validate = lambda x: len(x) > 0,
        error_messages={
            "required": "El nombre del pokemon es requerido"
        }
    )
    pokemonId = fields.Int (
        required = True,
        validate = lambda x: len(x) > 0,
        error_messages={
            "required": "El ID del pokemon es requerido"
        }
    )

    userName = fields.Str (
        required = True,
        validate = lambda x: len(x) > 0,
        error_messages={
            "required": "El nombre del usuario es requerido"
        }
    )


    