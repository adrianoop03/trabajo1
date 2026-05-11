from models.db import db

class vehicle(db.Model):
    __tablename__ = 'vehicle'

    patente = db.Column(db.String(100), primary_key=True, unique=True, nullable=False)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(45), nullable=False)
    nombre = db.Column(db.String(45), nullable=False)
    puertas = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(100), nullable=False)
    cilindrada = db.Column(db.Integer, nullable=False)

    def __init__(self, marca, modelo, nombre, puertas, color, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.nombre = nombre
        self.puertas = puertas
        self.color = color
        self.cilindrada = cilindrada

    def serialaize(self):
        return {
            'patente': self.patente,
            'marca': self.marca,
            'modelo': self.modelo,
            'nombre': self.nombre,
            'puertas': self.puertas,
            'color': self.color,
            'cilindrada': self.cilindrada
        }