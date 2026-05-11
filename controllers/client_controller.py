from models.client import client
from models.db import db 

def obtenerClientes():
    clientes=client.query.all()
    return[cliente.serialaize() for client in clients ]

def obtenerClienteid(id):
    client=client.query.get(id)
    if client:
        return client.serialaize()
    else:
        return None

def crearclientedatos(data):
    cliente_nuevo=client(**data)
    db.session.add(cliente_nuevo)
    db.session.commit()
    return cliente_nuevo.serialaize(),201

def borrarcliente(id):
    client=client.query.get(id)
    if client:
        db.session.delete(cliente)
        db.session.commit()
        return'',204
    else :
        return None,404