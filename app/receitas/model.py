from flask_sqlalchemy.model import Model
from app.extensions import db

class Receita(db.Model):
    __tablename__ = 'receita'
    id = db.Column(db.Interger,primary_key = True)
    remedio = db.Column(db.String,nullable = False)
    #medico
    #paciente