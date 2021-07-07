from flask import request,Blueprint
from app.consultas.model import Consulta
from app.extensions import db

consulta_api = Blueprint('consulta_api',__name__)

@consulta_api.route('/consultas', methods = ['POST'])
def criar_consulta():
    """criar_consulta(None)-> tuple(dict,int)
    Cria no banco de dados uma instancia de uma consulta e caso seja bem sucedido, 
    retorna os dados da consulta no formato json e uma mensagem de sucesso (200)"""
    if request.method == 'POST':
        dados = request.json
        data = dados.get("data")
        motivo = dados.get("motivo")
        if not (isinstance(data,str) or isinstance(motivo,str)):
            return {'Error': "Data ou Motivo da Consulta com Tipo Inválido"}
        consulta = Consulta(data=data, motivo=motivo)
        db.session.add(consulta)
        db.session.commit()
        return consulta.json(), 200