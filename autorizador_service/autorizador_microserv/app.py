from autorizador_microserv import create_app
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_jwt_extended.utils import get_jwt_identity
from flask_restful import Resource
from flask import jsonify
from flask_jwt_extended import jwt_required, create_access_token
from .logger import Logger
from flask import request

logs = Logger()

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

@app.route("/login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]
    if username != "test" or password != "test":
        logs.info('autorizador-service', 'post - usuario no autorizado', username)
        return jsonify({"msg": "Mal username or password"}), 401
    logs.info('autorizador-service', 'post - usuario autorizado', username)
    token_de_acceso = create_access_token(identity = username)
    logs.info('autorizador-service', 'post - token acceso', token_de_acceso)
    return jsonify(access_token=token_de_acceso)

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    logs.info('autorizador-service', 'get', 'Identificacion de acceso para el usuario actual con get_jwt_identity')
    current_user = get_jwt_identity()
    logs.info('autorizador-service', 'get - Usuario actual se encuentra autenticado', current_user)
    return jsonify(logged_in_as=current_user), 200

jwt = JWTManager(app)