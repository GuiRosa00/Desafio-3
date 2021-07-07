from app.extensions import db
from app.medicos.model import Medico
from app.pacientes.model import Paciente
association_med_pac = db.Table('association_med_pac',db.Model.metadata,
db.Column('medico', db.Integer, db.ForeignKey('medico.id')),
db.Column('paciente', db.Integer, db.ForeignKey('paciente.id')))