from flask import request,Blueprint
from app.pacientes.model import Paciente
from app.extensions import db

paciente_api = Blueprint('paciente_api',__name__)

@paciente_api.route('/pacientes', methods = ['POST'])
def criar_paciente():
    """criar_paciente(None)-> tuple(dict,int)
    Cria no banco de dados uma instancia de um Paciente e caso seja bem sucedido, 
    retorna os dados do Paciente no formato json e uma mensagem de sucesso (200)"""
    if request.method == 'POST':
        dados = request.json
        #dados do paciente
        nome = dados.get("nome")
        genero = dados.get("genero")
        idade = dados.get("idade")
        rg = dados.get("rg")
        endereco = dados.get("endereco")
        cpf = dados.get("cpf")
        plano = dados.get("plano")
        estado_c = dados.get("estado")
        contato = dados.get("contato")
        data_str = [nome,genero,endereco,plano,estado_c]
        data_int = [idade,rg,cpf,contato]
        for data in data_str:
            if not isinstance(data,str): return {"Error": "Um dos Dados String não está tipado como str"}
        for data in data_int:
            if not isinstance(data,int): return {"Error": "Um dos Dados Inteiros não está tipado como int"}
        paciente = Paciente(nome=nome, genero=genero,idade=idade,rg=rg,endereco=endereco,cpf=cpf,plano=plano,estado_c=estado_c,contato=contato)
        db.session.add(paciente)
        db.session.commit()
        return paciente.json(), 200