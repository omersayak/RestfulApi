from datetime import datetime
from flask import request, jsonify, g, Blueprint
from api.app.models.order import Order, OrderSchema
from api.app.models.ordered_item import OrderedItem, OrderedItemSchema
from api.app import db
from api.routes import check_auth

orders_bp = Blueprint('orders', __name__)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
ordered_item_schema = OrderedItemSchema()

@orders_bp.route('/orders', methods=['GET'])
@check_auth
def get_orders():
    all_orders = Order.query.all()
    result = orders_schema.dump(all_orders)
    return jsonify(result)

@orders_bp.route('/orders/<int:order_id>', methods=['GET'])
@check_auth
def get_order(order_id):
    order = Order.query.get(order_id)
    return order_schema.jsonify(order)

@orders_bp.route('/orders', methods=['POST'])
@check_auth
def add_order():
    status = request.json['status']
    table_no = request.json['table_no']
    ordered_items = []

    for ordered_item_data in request.json['ordered_items']:
        ordered_item = ordered_item_schema.load(ordered_item_data)
        ordered_items.append(ordered_item)

    new_order = Order(status=status, table_no=table_no, ordered_items=ordered_items, user_id=g.user.id, order_time=datetime.now())

    db.session.add(new_order)
    db.session.commit()

    return order_schema.jsonify(new_order)

@orders_bp.route('/orders/<int:order_id>', methods=['PUT'])
@check_auth
def update_order(order_id):
    order = Order.query.get(order_id)

    status = request.json['status']
    table_no = request.json['table_no']
    ordered_items = []

    for ordered_item_data in request.json['ordered_items']:
        ordered_item = ordered_item_schema.load(ordered_item_data)
        ordered_items.append(ordered_item)

    order.status = status
    order.table_no = table_no
    order.ordered_items = ordered_items

    db.session.commit()

    return order_schema.jsonify(order)

@orders_bp.route('/orders/<int:order_id>', methods=['DELETE'])
@check_auth
def delete_order(order_id):
    order = Order.query.get(order_id)

    db.session.delete(order)
    db.session.commit()

    return order_schema.jsonify(order)