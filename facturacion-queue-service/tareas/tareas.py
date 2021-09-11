from celery import Celery
from .logger import Logger

celery = Celery('tasks', broker='redis://localhost:6379/0')
logger = Logger()

@celery.task(name="reporte_queue_solicitud")
def reporte_queue_solicitud(operacion, payload):
  logger.info('fac-queue-reporte', 'reporte_queue_solicitud', 'solicitud recibida')


@celery.task(name="reporte_queue_consulta")
def reporte_queue_consulta(operacion, payload):
  logger.info('fac-queue-reporte', 'reporte_queue_consulta', 'solicitud recibida')


@celery.task(name="registrar_servicio_medico")
def registrar_servicio_medico(operacion, payload):
  logger.info('fac-queue', 'registrar_servicio_medico', 'solicitud recibida')

@celery.task(name="generar_reporte")
def generar_reporte(operacion, payload):
  logger.info('fac-queue', 'generar_reporte_facturacion', 'solicitud recibida')

#celery -A tareas worker -l info -Q fact_queue -E
