from app import mongo
from app.models.super_clase import SuperClass

class User(SuperClass):
     def __init__(self):
        super().__init__("users")

     def find_all(self):
         raise NotImplementedError("No es necesario obtnener todos los usuarios")