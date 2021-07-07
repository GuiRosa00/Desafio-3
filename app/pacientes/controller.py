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
        endereco = dados.get("endereco")
        plano = dados.get("plano")
        estado = dados.get("estado")
        idade = dados.get("idade")
        rg = dados.get("rg")
        cpf = dados.get("cpf")
        contato = dados.get("contato")
        data_str = [(nome,'nome'),(genero,'genero'),(endereco,'endereco'),(plano, 'plano'),(estado,'estado')]
        data_int = [(idade,'idade'),(rg,'rg'),(cpf,'cpf'),(contato,'contato')]
        for data in data_str:
            if not isinstance(data[0],str): return {"Error": f"O Dado: {data[1]} não está tipado como str"}
        for data in data_int:
            if not isinstance(data[0],int): return {"Error": f"O Dado: {data[1]} não está tipado como int"}
        paciente = Paciente(nome=nome, genero=genero,endereco=endereco,plano=plano,estado_civil=estado,idade=idade,rg=rg,cpf=cpf,contato=contato)
        db.session.add(paciente)
        db.session.commit()
        return paciente.json(), 200