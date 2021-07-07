from app.extensions import db

class Receita(db.Model):
    __tablename__ = 'receita'
    id = db.Column(db.Integer,primary_key = True)
    remedio = db.Column(db.String,nullable = False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente= db.relationship('Paciente',backref='receita', uselist = False)
    def json(self):
        dic = {'id':self.id,
        'remedio': self.remedio,
        'ID do Médico': self.medico_id,
        'ID do Paciente': self.paciente}
        return dic