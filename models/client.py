from models.db import db

class client(db.Model):
    __tablename__ = 'clients'

    id=db.column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self,nombre,email,telefono):
        self.nombre=nombre
        self.email=email
        self.telefono=telefono

    def serialaize(self):
        return{
            'id':self.id,
            'nombre':self.nombre,
            'email':self.email,
            'telefono':self.telefono
        }