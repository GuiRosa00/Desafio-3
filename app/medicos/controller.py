from flask import request,Blueprint
from app.medicos.model import Medico
from app.extensions import db
from sqlalchemy.exc import IntegrityError 

medico_api = Blueprint('medico_api',__name__)

@medico_api.route('/medicos', methods = ['POST'])
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
        espec = dados.get("espec")
        estado = dados.get("estado")
        idade = dados.get("idade")
        rg = dados.get("rg")
        cpf = dados.get("cpf")
        contato = dados.get("contato")
        registro = dados.get("registro")
        data_str = [(nome,'nome'),(genero,'genero'),(endereco,'endereco'),(espec, 'espec'),(estado,'estado')]
        data_int = [(idade,'idade'),(rg,'rg'),(cpf,'cpf'),(contato,'contato'),(registro,'registro')]
        for data in data_str:
            if not isinstance(data[0],str): return {"Error": f"O Dado: {data[1]} não está tipado como str"}
        for data in data_int:
            if not isinstance(data[0],int): return {"Error": f"O Dado: {data[1]} não está tipado como int"}
        medico = Medico(nome=nome, genero=genero,endereco=endereco,espec=espec,estado=estado,idade=idade,rg=rg,cpf=cpf,contato=contato,registro = registro)
        db.session.add(medico)
        db.session.commit()
        return medico.json(), 200