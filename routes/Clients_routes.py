from flask import Blueprint, request, jsonify
from controllers.client_controller import (
    obtenerClientes,
    obtenerClienteid,
    crearclientedatos,
    borrarcliente,
)

clients_bp = Blueprint("clients", __name__)


# GET listar todos los clientes
@clients_bp.route("/clientes", methods=["GET"])
def get_clientes():
    clientes = obtenerClientes()
    return jsonify(clientes), 200


# GET  obtener cliente por id
@clients_bp.route("/clientes/<int:id>", methods=["GET"])
def get_cliente(id):
    cliente = obtenerClienteid(id)
    if cliente is None:
        return jsonify({"error": "Cliente no encontrado"}), 404
    return jsonify(cliente), 200


# POSTcrear un cliente
@clients_bp.route("/clientes", methods=["POST"])
def post_cliente():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400
    resultado, codigo = crearclientedatos(data)
    return jsonify(resultado), codigo


# DELETE borrar un cliente
@clients_bp.route("/clientes/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    resultado, codigo = borrarcliente(id)
    if resultado is None:
        return jsonify({"error": "Cliente no encontrado"}), 404
    return jsonify(resultado), codigo