from facturacion_microserv import create_app
from flask_restful import Api, Resource
from celery import Celery
from .logger import Logger

celery_app = Celery(__name__, broker='redis://127.0.0.1:6379/0')

@celery_app.task(name="generar_reporte")
def generar_reporte(*args):
  pass

logs = Logger()

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaServicioFacturacion(Resource):

  def get(self):
    logs.info('facturacion-service', 'get', 'generar reporte facturacion')
    args = ('generar', True)
    generar_reporte.apply_async(args=args, queue='fact_queue')

api.add_resource(VistaServicioFacturacion, '/facturar')
