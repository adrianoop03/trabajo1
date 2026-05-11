from models.vehicle import vehicle
from models.db import db

class location(db.Model):
    __tablename__ = 'location'

    num_lugar = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    patente = db.Column(db.String(100), nullable=False)
    ocupado = db.Column(db.Boolean, nullable=False)

    def __init__(self, num_lugar, patente, ocupado):
        self.num_lugar = num_lugar
        self.patente = patente
        self.ocupado = ocupado

    def serialaize(self):
        return {
            'num_lugar': self.num_lugar,
            'patente': self.patente,
            'ocupado': self.ocupado
        }