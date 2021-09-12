from facturacion_microserv import create_app
from flask_restful import Api, Resource
from .logger import Logger
from time import sleep

logs = Logger()

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaFacturacion(Resource):
  def post(self):
    logs.info('facturacion-service', 'post', 'respuesta solicitud de reporte')
    sleep(100)
    logs.info('facturacion-service', 'post', 'respuesta servicio de entrega reporte')


class GestionFacturacion(Resource):
  def post(self):
    logs.info('facturacion-service', 'post', 'registro de servicio medico realizado')
    sleep(5)
    logs.info('facturacion-service', 'post', 'respuesta servicio de registro medico realizado')

    

api.add_resource(VistaFacturacion, '/facturar')
api.add_resource(GestionFacturacion, '/registrar')
