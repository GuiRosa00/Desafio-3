from app.association import association_med_pac
from app.extensions import db

class Medico(db.Model):
    __tablename__ = 'medico'
    #definicao das variaveis
    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(30),nullable = False)
    genero = db.Column(db.String(10),nullable = False)
    idade = db.Column(db.Integer,nullable = False)
    rg = db.Column(db.Integer,unique = True, nullable = False)
    endereco = db.Column(db.String(50),nullable = False)
    cpf = db.Column(db.Integer,unique = True,nullable = False)
    espec = db.Column(db.String(20),nullable = False)
    estado = db.Column(db.String(10),nullable = False)
    contato = db.Column(db.Integer,nullable = False)
    registro = db.Column(db.Integer,unique = True,nullable = False)
    #variaveis relacionais
    exames = db.relationship('Exame',backref='medico')
    receitas= db.relationship('Receita',backref='medico')
    consultas= db.relationship('Consulta',backref='medico')