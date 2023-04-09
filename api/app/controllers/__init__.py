from api.app.models.category import Category
from api.app.models.menu import Menu
from api.app.models.order import Order
from api.app.models.user import User


class CateoryController:
    def get_categories():
        categories = Category.query.all()
        return categories
    

    def post_category(json_data):
        category_schema = CategorySchema()
        category = category_schema.load(json_data)
        category.save()
        return category

    def put_category(json_data,category_id):
        Category = Category.query.get(category_id)
        category_schema = CategorySchema()
        updated_category = category_schema.load(json_data)
        category.name = updated_category.name
        category.save()
        return category
    
    def delete_category(category_id):
        category = Category.query.get(category_id)
        category.delete()
        return category
    

class MenuController:
    def get_menus(category_id=None):
        if category_id is None:
            menus = Menu.query.all()
            return menus
        else:
            menus = Menu.query.filter_by(category_id=category_id).all()
            return menus
        

    def post_menu(json_data):
        menu_schema = MenuSchema()
        menu = menu_schema.load(json_data)
        menu.save()
        return menu
    
    def put_menu(json_data,menu_id):
        Menu = Menu.query.get(menu_id)
        menu_schema = MenuSchema()
        updated_menu = menu_schema.load(json_data)
        menu.name = updated_menu.name
        menu.price = updated_menu.price
        menu.save()
        return updated_menu
    
    def delete_menu(menu_id):
        menu = Menu.query.get(menu_id)
        menu.delete()
        return menu


class OrderController:
    def post_order(json_data):
        order_schema = OrderSchema()
        order = order_schema.load(json_data)
        order.save()
        return order
    
    def get_order(user_id=None):
        if user_id is None:
            orders = Order.query.all()
            return orders
        else:
            orders = Order.query.filter_by(user_id=user_id).all()
            return orders


    def put_order(json_data,order_id):
        Order = Order.query.get(order_id) 
        order_schema = OrderSchema()
        updated_order = order_schema.load(json_data)
        order.status = updated_order.status
        order.save()
        return updated_order


class UserController:
    def get_users(username):
        users = User.query.filter_by(username=username).first()
        return users
    
    def post_user(json_data):
        user_schema = UserSchema()
        user = user_schema.load(json_data)
        user.save()
        return user
    
"""
Yukarıdaki kod bloğu, `CategoryController`, `MenuController`, `OrderController` ve `UserController` sınıflarını içeriyor. Bu sınıflar Flask view fonksiyonlarını ilgili modellere bağlayan metotları taşıyorlar.

Örnek olarak `CategoryController` sınıfındaki `get_categories()` metodu, veritabanındaki tüm kategorileri alıyor ve bu kategorileri geri döndürüyor. Benzer şekilde, diğer metotlarda da ilgili model için istekler (GET, POST, PUT, DELETE) işleniyor.

"""