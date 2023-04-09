from flask import Blueprint, request, jsonify, g
from app.controllers import menu_controller, order_controller
from routes.auth import auth

menu_bp = Blueprint("menu", __name__, url_prefix="/api/v1/menus")
order_bp = Blueprint("order", __name__, url_prefix="/api/v1/orders")

# Menus endpointleri
@menu_bp.route("/", methods=["GET"])
def get_menus():
    menus = menu_controller.get_all_menus()
    return jsonify(menus)


@menu_bp.route("/<menu_id>", methods=["GET"])
def get_menu_by_id(menu_id):
    menu = menu_controller.get_menu_by_id(menu_id)
    return jsonify(menu)


@menu_bp.route("/", methods=["POST"])
@auth.login_required
def create_menu():
    request_json = request.json
    new_menu = menu_controller.create_menu(request_json)
    return jsonify(new_menu)


@menu_bp.route("/<menu_id>", methods=["PUT"])
@auth.login_required
def update_menu(menu_id):
    request_json = request.json
    updated_menu = menu_controller.update_menu(menu_id, request_json)
    return jsonify(updated_menu)


@menu_bp.route("/<menu_id>", methods=["DELETE"])
@auth.login_required
def delete_menu(menu_id):
    menu_controller.delete_menu(menu_id)
    return "", 204

# Orders endpointleri
@order_bp.route("/", methods=["POST"])
def create_order():
    request_json = request.json
    new_order = order_controller.create_order(request_json)
    return jsonify(new_order)


@order_bp.route("/", methods=["GET"])
@auth.login_required
def get_orders():
    orders = order_controller.get_orders_by_user_id(g.user.id)
    return jsonify(orders)


@order_bp.route("/<order_id>", methods=["DELETE"])
@auth.login_required
def cancel_order(order_id):
    order_controller.cancel_order(order_id)
    return "", 204