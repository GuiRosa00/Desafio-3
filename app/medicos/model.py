from app.association import association_med_pac
from app.extensions import db

class Medico(db.Model):
    __tablename__ = 'medico'
    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(30),nullable = False)
    genero = db.Column(db.String(10),nullable = False)
    idade = db.Column(db.Integer,nullable = False)
    rg = db.Column(db.Integer,unique = True, nullable = False)
    endereco = db.Column(db.String(50),nullable = False)
    cpf = db.Column(db.Integer,unique = True,nullable = False)
    espec = db.Column(db.String(20),nullable = False)
    estado = db.Column(db.String(10),nullable = False)
    contato = db.Column(db.String(13),nullable = False)
    registro = db.Column(db.Integer,unique = True,nullable = False)
    exames = db.relationship('Exame',backref='medico')
    receitas= db.relationship('Receita',backref='medico')
    consultas= db.relationship('Consulta',backref='medico')
    medicos= db.relationship('Paciente',secondary = association_med_pac, backref = db.backref('medicos', lazy = 'dynamic'))