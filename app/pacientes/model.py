from app.extensions import db
from app.association import association_med_pac

class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(30),nullable = False)
    genero = db.Column(db.String(10),nullable = False)
    idade = db.Column(db.Integer,nullable = False)
    rg = db.Column(db.Integer,unique = True, nullable = False)
    endereco = db.Column(db.String(50),nullable = False)
    cpf = db.Column(db.Integer,unique = True,nullable = False)
    plano = db.Column(db.String(20),nullable = False)
    estado_civil = db.Column(db.String(10),nullable = False)
    contato = db.Column(db.String(13),unique = True,nullable = False)
    exames = db.relationship('Exame',backref='paciente')
    receita_id= db.Column(db.Integer,db.ForeignKey('receita.id'))
    consultas= db.relationship('Consulta',backref='paciente')
    pacientes= db.relationship('Medico',secondary = association_med_pac, backref = db.backref('pacientes', lazy = 'dynamic'))