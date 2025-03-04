from flask import jsonify
#Creamos este desmadre para no escribir tanto pinche jsnonify
#Se van a mandar a llamar cuando se ocupe una respuesta
class ResponseManager:
    def succes(self, data):
        if isinstance(data,str):
            data={
                "message":data
            }

        return jsonify(data),200 # el numero va afuera
    
    def error(self,data="Invalid request"):
            if isinstance(data, str):
                data={
                    "message":data
                }

            return jsonify(data),400 # el numero va afuera
    
    def error_server(self,data="SERVER ERROR"):
            if isinstance(data,str):
                data={
                    "message":data
                }

            return jsonify(data),500 # el numero va afuera