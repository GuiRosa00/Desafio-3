from app.extensions import db

class Receita(db.Model):
    __tablename__ = 'receita'
    id = db.Column(db.Interger,primary_key = True)
    remedio = db.Column(db.String,nullable = False)
    #medico_id = db.Column(db.Interger, db.ForeignKey('medico.id'))
    #paciente_id = db.Column(db.Interger, db.ForeignKey('paciente.id'))