from flask import Flask
from app.config import config
from app.extensions import db,migrate
from app.consultas.controller import consulta_api

from app.consultas import model
from app.exames import model
from app.medicos import model
from app.pacientes import model
from app.receitas import model

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(consulta_api)
    db.init_app(app)
    migrate.init_app(app,db)
    return app
