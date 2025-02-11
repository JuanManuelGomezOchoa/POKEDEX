from app import mongo

class PokemonSaved:
    collection = mongo.db.pokemonsSaved

    @staticmethod
    def find_all():
        pokemonsSaved = PokemonSaved.collection.find()
        return list(pokemonsSaved)
    
    @staticmethod
    def find_by_id(pokemonSaved_id):
        pokemonSaved = PokemonSaved.collection.find_one({
            "_id": pokemonSaved_id
        })
        return pokemonSaved
    
    @staticmethod
    def create(data):
        pokemonSaved = PokemonSaved.collection.insert_one(data)
        return pokemonSaved.inserted_id
    
    @staticmethod
    def update(pokemonSaved_id, data):
        pokemonSaved = PokemonSaved.collection.update_one({
            "_id":pokemonSaved_id
        },{
            "$set":data
        })
        return pokemonSaved
    
    @staticmethod
    def delete(pokemonSaved_id):
        return PokemonSaved.collection.delete_one({"_id":pokemonSaved_id})