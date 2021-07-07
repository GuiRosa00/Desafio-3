from app.extensions import db
from app.association import association_med_pac

class Paciente(db.Model):
    __tablename__ = 'paciente'
    #definicao das variaveis
    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(30),nullable = False)
    genero = db.Column(db.String(10),nullable = False)
    idade = db.Column(db.Integer,nullable = False)
    rg = db.Column(db.Integer,unique = True, nullable = False)
    endereco = db.Column(db.String(50),nullable = False)
    cpf = db.Column(db.Integer,unique = True,nullable = False)
    plano = db.Column(db.String(20),nullable = False)
    estado_c = db.Column(db.String(10),nullable = False)
    contato = db.Column(db.Integer,unique = True,nullable = False)
    #variaveis relacionais
    exames = db.relationship('Exame',backref='paciente')
    receita_id= db.Column(db.Integer,db.ForeignKey('receita.id'))
    consultas= db.relationship('Consulta',backref='paciente')
    pacientes= db.relationship('Medico',secondary = association_med_pac, backref = db.backref('pacientes', lazy = 'dynamic'))