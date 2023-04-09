from app.controllers.menu_controller import MenuController

class TestMenu:
    def setup_method(self):
        self.controller = MenuController()

    def test_create_menu(self):
        res = self.controller.create({'name': 'test_menu', 'price': 10.99})
        assert res['name'] == 'test_menu'
        assert res['price'] == 10.99

    def test_get_all_menus(self):
        res = self.controller.get_all()
        assert res == []

    def test_update_menu(self):
        menu = self.controller.create({'name': 'test_menu', 'price': 10.99})
        res = self.controller.update(menu['id'], {'name': 'new_test_menu', 'price': 12.99})
        assert res['name'] == 'new_test_menu'
        assert res['price'] == 12.99
        assert res['id'] == menu['id']

    def test_delete_menu(self):
        menu = self.controller.create({'name': 'test_menu', 'price': 10.99})
        res = self.controller.delete(menu['id'])
        assert res == True