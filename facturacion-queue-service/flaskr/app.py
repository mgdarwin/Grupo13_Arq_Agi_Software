from flaskr import create_app
from flask_restful import Api
from .vistas.VistaGestionMedica import VistaGestionMedica
from .vistas.VistaReporte import VistaReporte

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaReporte, '/mensaje/reporte')
api.add_resource(VistaGestionMedica, '/mensaje/medica')