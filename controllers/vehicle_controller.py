from models.vehicle import vehicle
from models.db import db 

def obtenerVehiculos():
    vehcile=vehicle.query.all()
    return[vehicle.serialaize() for vehicle in vehicle ]


def registrarvehiculo(data):
    vehiculo_nuevo=vehicle(**data)
    vehiculo_existe=vehicle.query.get(vehiculo_nuevo.patente)
    if vehiculo_existe:
        return("error la patente ya existe"),400
    elif not vehiculo_existe:
        db.session.add(vehiculo_nuevo)
        db.session.commit()
        return vehiculo_nuevo.serialize(),201
    else:
        return ("error "),500

def borrarvehiculo(patente):
    vehicle=vehicle.query.get(patente)
    if vehicle:
        db.session.delete(vehicle)
        db.session.commit()
        return'',204
    else :
        return "patente no encontrada",404