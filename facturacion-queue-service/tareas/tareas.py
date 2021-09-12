from celery import Celery
from .logger import Logger
import requests

celery = Celery('tasks', broker='redis://localhost:6379/0')
logger = Logger()

@celery.task(name="reporte_queue_solicitud")
def reporte_queue_solicitud(operacion, payload):
  logger.info('facturacion-queue-service', 'reporte_queue_solicitud', 'solicitud reporte recibida')
  content = requests.post('http://127.0.0.1:5002/facturar')

@celery.task(name="reporte_queue_consulta")
def reporte_queue_consulta(operacion, payload):
  logger.info('facturacion-queue-service', 'reporte_queue_consulta', 'consulta reporte recibida')
  content = requests.post('http://127.0.0.1:5002/facturar')

@celery.task(name="registrar_servicio_medico")
def registrar_servicio_medico(operacion, payload):
  logger.info('facturacion-queue-service', 'registrar_servicio_medico', 'solicitud registro servicio recibida')
  content = requests.post('http://127.0.0.1:5002/registrar')
  

#celery -A tareas worker -l info -Q fact_queue -E
