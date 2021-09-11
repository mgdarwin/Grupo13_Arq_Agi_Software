from facturacion_microserv import create_app
from flask_restful import Api, Resource
from celery import Celery
from .logger import Logger
from time import sleep

celery_app = Celery(__name__, broker='redis://127.0.0.1:6379/0')

logs = Logger()

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaFacturacion(Resource):
  def post(self):
    logs.info('facturacion-service', 'post', 'respuesta solicitud de reporte')
    args = ('generar', True)


class GestionFacturacion(Resource):
  def post(self):
    logs.info('facturacion-service', 'post', 'registro de servicio medico realizado')
    args = ('generar', True)
    

api.add_resource(VistaFacturacion, '/facturar')
api.add_resource(GestionFacturacion, '/registrar')




# @celery_app.task(name="reporte_queue_solicitud")
# def reporte_queue_solicitud():
#     logs.info('facturacion-service', 'reporte_queue_solicitud', 'generar reporte facturacion')
#     args = ('generar', True)

# @celery_app.task(name="reporte_queue_consulta")
# def reporte_queue_consulta():
#     logs.info('facturacion-service', 'reporte_queue_consulta', 'retorna consulta facturacion')
#     args = ('generar', True)

# @celery_app.task(name="registrar_servicio_medico")
# def registrar_servicio_medico():
#     logs.info('facturacion-service', 'registrar_servicio_medico', 'registra servicio para facturacion')
#     args = ('generar', True)

# class VerificaCola(): 
#   def verifica_cola(self):
#     logs.info('facturacion-service', 'registrar_servicio_medico', 'se instancia')
#     reporte_queue_solicitud()

# verificar = VerificaCola()
# verificar.verifica_cola()