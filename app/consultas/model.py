from app.extensions import db

class Consulta(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Interger,primary_key = True)
    data = db.Column(db.Interger,nullable = False)
    motivo = db.Column(db.String(20),nullable = False)
