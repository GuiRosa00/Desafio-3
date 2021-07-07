from app.extensions import db

class Exame(db.Model):
    __tablename__ = 'exame'
    id = db.Column(db.Integer,primary_key = True)
    tipo = db.Column(db.String(20),nullable = False)
    data = db.Column(db.Integer,nullable = False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))