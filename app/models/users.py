from app import mongo
from app.models.super_clase import SuperClass
class User(SuperClass):
    def _init_(self):
        super()._init_("users")#llama a la clase padre, lo iniciamos y ese wey ya espera la collecion

    def create(self, data):
        super().create(self, data)

    def find_all(self):
        raise NotImplementedError("No es necesario traer todos los usuarios")
    
    def find_by_id(self, object_id):
        super().find_by_id(object_id)
       
    def delete(self, object_id):
        super().delete(self, object_id)
      
    def update(self, object_id, data):
        super().update(self, object_id, data)

    def get_by_email_password(self, email, password):
        user = self.collection.find_one({"email": email, "password":password})
        user["_id"]=str(user["_id"])
        return user