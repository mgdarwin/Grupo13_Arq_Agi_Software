from flask import request
from flask_restful import Resource
from datetime import datetime
from ..tareas import registrar_log 

class VistaReporte(Resource):

    def post(self):
        id_reporte = request.json["idreport"]
        registrar_log.delay(id_reporte, datetime.utcnow())
        return {'mensaje':'Mensaje Reporte Creado exitoso'}, 200