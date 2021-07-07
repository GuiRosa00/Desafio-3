from flask import Flask
from app.config import Config
from app.extensions import db,migrate

from app.consultas.controller import consulta_api
from app.exames.controller import exame_api
from app.receitas.controller import receita_api
from app.pacientes.controller import paciente_api
from app.medicos.controller import medico_api

from app.consultas import model
from app.exames import model
from app.medicos import model
from app.pacientes import model
from app.receitas import model

def create_app():
    """create_app(None)-> object
    Cria o app do Flask utilizado como back-end do sistema"""
    app = Flask(__name__)
    app.config.from_object(Config)
    #metodos registrados pelo Blueprint
    app.register_blueprint(consulta_api)
    app.register_blueprint(exame_api)
    app.register_blueprint(receita_api)
    app.register_blueprint(paciente_api)
    app.register_blueprint(medico_api)
    db.init_app(app)
    migrate.init_app(app,db)
    return app
