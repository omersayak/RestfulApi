from app.controllers.order_controller import OrderController

class TestOrder:
    def setup_method(self):
        self.controller = OrderController()

    def test_create_order(self):
        res = self.controller.create({'menu_id': 1, 'user_id': 1})
        assert res['menu_id'] == 1
        assert res['user_id'] == 1

    def test_get_all_orders(self):
        res = self.controller.get_all()
        assert res == []

    def test_update_order(self):
        order = self.controller.create({'menu_id': 1, 'user_id': 1})
        res = self.controller.update(order['id'], {'menu_id': 2, 'user_id': 2})
        assert res['menu_id'] == 2
        assert res['user_id'] == 2
        assert res['id'] == order['id']

    def test_delete_order(self):
        order = self.controller.create({'menu_id': 1, 'user_id': 1})
        res = self.controller.delete(order['id'])
        assert res == True