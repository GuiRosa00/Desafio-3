from app.extensions import db

class Receita(db.Model):
    __tablename__ = 'receita'
    #definicao das variaveis
    id = db.Column(db.Integer,primary_key = True)
    remedio = db.Column(db.String(50),nullable = False)
    #variaveis relacionais
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente= db.relationship('Paciente',backref='receita', uselist = False)
    
    def json(self):
        """json(self)-> dict
        Retorna os dados de uma Receita no formato JSON"""
        dic = {'id':self.id,
        'remedio': self.remedio,
        'ID do Médico': self.medico_id,
        'ID do Paciente': self.paciente}
        return dic