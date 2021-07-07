from app.extensions import db

class Medico(db.Model):
    __tablename__ = 'medico'
    id = db.Column(db.Interger,primary_key = True)
    nome = db.Column(db.String(30),nullable = False)
    genero = db.Column(db.String(10),nullable = False)
    idade = db.Column(db.Interger,nullable = False)
    rg = db.Column(db.Interger,unique = True, nullable = False)
    endereco = db.Column(db.String(50),nullable = False)
    cpf = db.Column(db.Interger,unique = True,nullable = False)
    espec = db.Column(db.String(20),nullable = False)
    estado = db.Column(db.String(10),nullable = False)
    contato = db.Column(db.String(13),nullable = False)
    registro = db.Column(db.Interger,unique = True,nullable = False)
    #paciente
    #receita
    #exame
    #consulta