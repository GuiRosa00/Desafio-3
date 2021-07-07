from flask import request,Blueprint
from app.exames.model import Exame
from app.extensions import db

exame_api = Blueprint('exame_api',__name__)

@exame_api.route('/exames', methods = ['POST'])
def criar_exame():
    """criar_exame(None)-> tuple(dict,int)
    Cria no banco de dados uma instancia de um Exame e caso seja bem sucedido, 
    retorna os dados do Exame no formato json e uma mensagem de sucesso (200)"""
    if request.method == 'POST':
        dados = request.json
        data = dados.get("data")
        tipo = dados.get("tipo")
        if not (isinstance(data,str) or isinstance(tipo,str)):
            return {'Error': "Data ou Tipo de Exame com Tipo Inválido (diferente de str)"}
        exame = Exame(data=data, tipo=tipo)
        db.session.add(exame)
        db.session.commit()
        return exame.json(), 200