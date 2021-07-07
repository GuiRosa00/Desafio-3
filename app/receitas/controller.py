from flask import request,Blueprint
from app.receitas.model import Receita
from app.extensions import db

receita_api = Blueprint('receita_api',__name__)

@receita_api.route('/receitas', methods = ['POST'])
def criar_receita():
    """criar_exame(None)-> tuple(dict,int)
    Cria no banco de dados uma instancia de uma Receita e caso seja bem sucedido, 
    retorna os dados da Receita no formato json e uma mensagem de sucesso (200)"""
    if request.method == 'POST':
        dados = request.json
        remedio = dados.get("remedio")
        if not (isinstance(remedio,str)):
            return {'Error': "Remédio com Tipo Inválido"}
        receita = Receita(remedio = remedio)
        db.session.add(receita)
        db.session.commit()
        return receita.json(), 200