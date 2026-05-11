from flask import Blueprint, request, jsonify
from controllers.location_controller import (
    obtenerLugar,
    obtenerlugarid,
    obtenerlugarvacio,
    ocuparlugar,
    desocuparlugar,
)

locations_bp = Blueprint("locations", __name__)


# GET todos los lugares
@locations_bp.route("/lugares", methods=["GET"])
def get_lugares():
    lugares = obtenerLugar()
    return jsonify(lugares), 200


# GET lugares disponibles
@locations_bp.route("/lugares/vacios", methods=["GET"])
def get_lugares_vacios():
    lugares = obtenerlugarvacio()
    if lugares is None:
        return jsonify({"mensaje": "No hay lugares disponibles"}), 404
    return jsonify(lugares), 200


# GET  obtener lugar por número
@locations_bp.route("/lugares/<int:num_lugar>", methods=["GET"])
def get_lugar(num_lugar):
    lugar = obtenerlugarid(num_lugar)
    if lugar is None:
        return jsonify({"error": "Lugar no encontrado"}), 404
    return jsonify(lugar), 200


# PUT marcar lugar como ocupado
@locations_bp.route("/lugares/<int:num_lugar>/ocupar", methods=["PUT"])
def put_ocupar(num_lugar):
    resultado, codigo = ocuparlugar(num_lugar)
    return jsonify(resultado), codigo


# PUT  marcar lugar como libre
@locations_bp.route("/lugares/<int:num_lugar>/desocupar", methods=["PUT"])
def put_desocupar(num_lugar):
    resultado, codigo = desocuparlugar(num_lugar)
    return jsonify(resultado), codigo