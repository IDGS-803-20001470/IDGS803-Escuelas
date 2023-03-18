from flask_sqlalchemy import SQLAlchemy

import datetime

db=SQLAlchemy()

class Alumnos(db.Model):
    __tablename__='alumnos'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apellidos=db.Column(db.String(100))
    create_date=db.Column(db.DateTime, default=datetime.datetime.now)
    email=db.Column(db.String(50))
  
class Profesores(db.Model):
    __tablename__='profesores'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apellidos=db.Column(db.String(100))
    create_date=db.Column(db.DateTime, default=datetime.datetime.now)
    email=db.Column(db.String(50))
    materia=db.Column(db.String(50))


  