from app.extensions import db

class Consulta(db.Model): 
    __tablename__ = 'consulta'
    #definicao das variaveis
    id = db.Column(db.Integer,primary_key = True)
    data = db.Column(db.String(8),nullable = False)
    motivo = db.Column(db.String(50),nullable = False)
    #variaveis relacionais
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    
    def json(self):
        """json(self)-> dict
        Retorna os dados de uma consulta no formato JSON"""
        dic = {'id':self.id,
        'Data da Consulta': self.data,
        'Motivo da Consulta': self.motivo,
        'ID do Médico': self.medico_id,
        'ID do Paciente': self.paciente_id}
        return dic