from app.extensions import db

class Consulta(db.Model):
    __tablename__ = 'consulta'
    id = db.Column(db.Integer,primary_key = True)
    data = db.Column(db.Integer,nullable = False)
    motivo = db.Column(db.String(20),nullable = False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    def json(self):
        dic = {'id':self.id,
        'data': self.data,
        'motivo': self.motivo,}
        return dic