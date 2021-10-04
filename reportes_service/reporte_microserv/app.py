from reporte_microserv import create_app
from flask_restful import Api, Resource
from celery import Celery
from .logger import Logger
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

# celery_app = Celery(__name__, broker='redis://127.0.0.1:6379/0')

# @celery_app.task(name="reporte_queue_solicitud")
def reporte_queue_solicitud(*args):
  pass

# @celery_app.task(name="reporte_queue_consulta")
def reporte_queue_consulta(*args):
  pass

logs = Logger()

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaReporte(Resource):
  @jwt_required()
  def post(self):
    # url = ''
    # response = requests.request("POST", url=url, headers=headers)
    # user = response.json()
    # is_authorized = user.is_authorized()
    is_authorized = True
    if is_authorized:
      logs.info('reporte-service', 'post', 'enviar solicitud de reporte')
      args = ('generar', True)
      reporte_queue_solicitud.apply_async(args=args, queue='fact_queue')

  @jwt_required()
  def get(self):
    # url = ''
    # response = requests.request("POST", url=url, headers=headers)
    # user = response.json()
    # is_authorized = user.is_authorized()
    is_authorized = True
    if is_authorized:
      logs.info('reporte-service', 'get', 'consultar estado de reporte')
      args = ('consultar', True)
      reporte_queue_consulta.apply_async(args=args, queue='fact_queue')


api.add_resource(VistaReporte, '/reporte')
