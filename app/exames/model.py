from app.extensions import db

class Exame(db.Model):
    __tablename__ = 'exame'
    #definição das variaveis
    id = db.Column(db.Integer,primary_key = True)
    tipo = db.Column(db.String(20),nullable = False)
    data = db.Column(db.String(8),nullable = False)
    #variaveis relacionais
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    
    def json(self):
        """json(self)-> dict
        Retorna os dados de um exame no formato JSON"""
        dic = {'id':self.id,
        'data': self.data,
        'tipo de exame': self.tipo,
        'ID do Médico': self.medico_id,
        'ID do Paciente': self.paciente_id}
        return dic