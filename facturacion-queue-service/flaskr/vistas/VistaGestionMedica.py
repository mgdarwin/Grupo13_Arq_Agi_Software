from flask import request
from flask_restful import Resource
from datetime import datetime
from ..tareas import registrar_log 

class VistaGestionMedica(Resource):
    def post(self):
        id_factura = request.json["idfactura"]
        registrar_log.delay(id_factura, datetime.utcnow())
        return {'mensaje':'Mensaje Factura Creado exitoso'}, 200