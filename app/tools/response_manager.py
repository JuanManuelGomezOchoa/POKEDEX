from flask import jsonify

class ResponseManager:
    def succes(self, data):
        if isinstance(data == "str"):
            data = {
                "message":data #Cambiamos el data de texto a un objeto
            }
        return jsonify(data),200
    
    def error(self, data="Invalid request"):
        if isinstance(data == "str"):
            data = {
                "message":data
            }
        return jsonify(data),400
    
    def error_server(self, data="SERVER ERROR"):
        if isinstance(data == "str"):
            data = {
                "message":data
            }
        return jsonify(data),500