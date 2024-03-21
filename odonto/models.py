from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Paciente(db.Model):  # tabela paciente

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_paciente = db.Column(db.String)
    sexo = db.Column(db.String)
    data_nasc = db.Column(db.String) 
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    logradouro = db.Column(db.String)
    numero = db.Column(db.String)
    bairro = db.Column(db.String)
    cep = db.Column(db.String)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)
    email = db.Column(db.String)
    telefone = db.Column(db.String)


class Profissional(db.Model):  # tabela profissional

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_profissional = db.Column(db.String)
    sexo = db.Column(db.String)
    cro = db.Column (db.String)
    data_nasc = db.Column(db.String) 
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    logradouro = db.Column(db.String)
    numero = db.Column(db.String)
    bairro = db.Column(db.String)
    cep = db.Column(db.String)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)
    email = db.Column(db.String)
    telefone = db.Column(db.String)
    horarios = db.relationship('Agendamento', backref='profissional', lazy=True)


class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    horario = db.Column(db.String(5))  # Formato HH:MM
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissional.id'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    paciente = db.relationship('Paciente', backref=db.backref('agendamentos', lazy=True))





