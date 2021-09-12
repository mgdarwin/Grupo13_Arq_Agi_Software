from reporte_microserv import create_app
from flask_restful import Api, Resource
from celery import Celery
from .logger import Logger

celery_app = Celery(__name__, broker='redis://127.0.0.1:6379/0')

@celery_app.task(name="reporte_queue_solicitud")
def reporte_queue_solicitud(*args):
  pass

@celery_app.task(name="reporte_queue_consulta")
def reporte_queue_consulta(*args):
  pass

logs = Logger()

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaReporte(Resource):

  def post(self):
    logs.info('reporte-service', 'post', 'enviar solicitud de reporte')
    args = ('generar', True)
    reporte_queue_solicitud.apply_async(args=args, queue='fact_queue')

  def get(self):
    logs.info('reporte-service', 'get', 'consultar estado de reporte')
    args = ('consultar', True)
    reporte_queue_consulta.apply_async(args=args, queue='fact_queue')


api.add_resource(VistaReporte, '/reporte')
