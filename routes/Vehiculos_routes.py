from flask import Blueprint, request, jsonify
from controllers.vehicle_controller import obtenerVehiculos, registrarvehiculo, borrarvehiculo
 
vehiculos_bp = Blueprint("vehiculos", __name__)
 
 
# GET listar todos los vehículos
@vehiculos_bp.route("/vehiculos", methods=["GET"])
def get_vehiculos():
    vehiculos = obtenerVehiculos()
    return jsonify(vehiculos), 200
 
 
# POST registrar un vehículo
@vehiculos_bp.route("/vehiculos", methods=["POST"])
def post_vehiculo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400
    resultado, codigo = registrarvehiculo(data)
    return jsonify(resultado), codigo
 
 
# DELETE borrar un vehículo por patente
@vehiculos_bp.route("/vehiculos/<string:patente>", methods=["DELETE"])
def delete_vehiculo(patente):
    resultado, codigo = borrarvehiculo(patente)
    if resultado is None:
        return jsonify({"error": "Vehículo no encontrado"}), 404
    return jsonify(resultado), codigo
 