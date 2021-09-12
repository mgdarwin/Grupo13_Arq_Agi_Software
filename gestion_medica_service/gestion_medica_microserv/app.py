from gestion_medica_microserv import create_app
from flask_restful import Api, Resource
from celery import Celery
from .logger import Logger

celery_app = Celery(__name__, broker='redis://127.0.0.1:6379/0')

@celery_app.task(name="registrar_servicio_medico")
def registrar_servicio_medico(*args):
  pass

logs = Logger()

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaServicioMedico(Resource):

  def post(self):
    logs.info('gestion-medica-service', 'post', 'registrar servicio medico')
    args = ('registrar', True)
    registrar_servicio_medico.apply_async(args=args, queue='fact_queue')


api.add_resource(VistaServicioMedico, '/servicio')
