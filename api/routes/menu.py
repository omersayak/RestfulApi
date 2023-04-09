from flask import request, jsonify
from api.app.models.menu import Menu,MenuSchema
from api.app import db
from api.routes import bp


menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)


@bp.route('/menus', methods=['GET'])
def get_menus():
    all_menus = Menu.query.all()
    result = menus_schema.dump(all_menus)
    return menus_schema.dump(result)

@bp.route('/menus/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
    menu = Menu.query.get(menu_id)
    return menu_schema.jsonify(menu)


@bp.route('/menus', methods=['POST'])
def add_menu():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    category_id = request.json['category_id']


    new_menu = Menu(name=name,description=description,price=price,category_id=category_id)


    db.session.add(new_menu)
    db.session.commit()
    return menu_schema.jsonify(new_menu)


@bp.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    menu = Menu.query.get(menu_id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    category_id = request.json['category_id']


    menu.name = name
    menu.description = description
    menu.price = price
    menu.category_id = category_id

    db.session.commit()

    return menu_schema.jsonify(menu)


@bp.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id):
    menu = Menu.query.get(menu_id)
    db.session.delete(menu)
    db.session.commit()
    return menu_schema.jsonify(menu)