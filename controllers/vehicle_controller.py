from models.vehicle import vehicle
from models.db import db 
 
def obtenerVehiculos():
    vehiculos = vehicle.query.all()
    return [v.serialaize() for v in vehiculos]
 
 
def registrarvehiculo(data):
    vehiculo_nuevo = vehicle(**data)
    vehiculo_existe = vehicle.query.get(vehiculo_nuevo.patente)
    if vehiculo_existe:
        return {"error": "la patente ya existe"}, 400
    else:
        db.session.add(vehiculo_nuevo)
        db.session.commit()
        return vehiculo_nuevo.serialaize(), 201
 
def borrarvehiculo(patente):
    vehiculo = vehicle.query.get(patente)
    if vehiculo:
        db.session.delete(vehiculo)
        db.session.commit()
        return {"mensaje": "vehiculo eliminado"}, 204
    else:
        return {"error": "patente no encontrada"}, 404