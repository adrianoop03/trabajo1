from models.db import db

class vehicle(db.Model):
    _tablename__ = 'vehicle'

    patente=db.column(db.String(1000), primary_key=True, unique=True, nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(45), nullable=False)
    nombre = db.Column(db.String(45), nullable=False)
    puertas = db.column(db.Integer,  nullable=False)
    color = db.column(db.string(100), nullable=False)
    cilindrada = db.column(db.Integer, nullable=false)

    def __init__(self,marca,modelo,nombre,puertas,color,cilindrada):
        self.marca=marca
        self.modelo=modelo
        self.nombre=nombre
        self.puertas=puertas
        self.color=color
        self.cilindrada=cilindrada

    def serialaize(self):
        return{
            'patente':self.patente,
            'modelo':self.modelo,
            'nombre':self.nombre,
            'puertas':self.puertas
            'color':self.color
            'cilindrada':self.cilindrada
        }