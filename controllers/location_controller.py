from models.location import location
from models.db import db 

def obtenerLugar():
    locations=location.query.all()
    return[location.serialaize() for location in locations ]

def obtenerlugarid(num_lugar):
    location=location.query.get(num_lugar)
    if location:
        return location.serialaize()
    else:
        return None

def obtenerlugarvacio():
    location=location.query.filter_by(ocupado=False).all()
    if location:
        return [location.serialaize() for location in locations]
    else:
        return None

def ocuparlugar(num_lugar):
    location=location.query.get(num_lugar)
    if not location:
        return("error estacionamiento no encontrado "),404
    if location.ocupado:
        return("error el estacionamiento ya esta ocupado"),400
    if location and not location.ocupado:
        location.ocupado=True
        db.session.commit()
    return location.serialaize(),200


def desocuparlugar(num_espacio):
    location=location.query.get(num_lugar)
    if not location:
        return("error estacionamiento no encontrado "),404
    if location.ocupado:
        return("error el estacionamiento ya esta desocupado"),400
    if location and not location.ocupado:
        location.ocupado=True
        db.session.commit()
    return location.serialaize(),200
