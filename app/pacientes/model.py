from app.extensions import db

class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Interger,primary_key = True)
    nome = db.Column(db.String(30),nullable = False)
    genero = db.Column(db.String(10),nullable = False)
    idade = db.Column(db.Interger,nullable = False)
    rg = db.Column(db.Interger,unique = True, nullable = False)
    endereco = db.Column(db.String(50),nullable = False)
    cpf = db.Column(db.Interger,unique = True,nullable = False)
    plano = db.Column(db.String(20),nullable = False)
    estado_civil = db.Column(db.String(10),nullable = False)
    contato = db.Column(db.String(13),unique = True,nullable = False)#evitar telefones inexistentes
    exames = db.relationship('Exame',backref='paciente')
    receitas= db.relationship('Receita',backref='paciente')
    consultas= db.relationship('Consulta',backref='paciente')
    #medico