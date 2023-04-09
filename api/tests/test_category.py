from app.controllers.category_controller import CategoryController

class TestCategory:
    def setup_method(self):
        self.controller = CategoryController()

    def test_create_category(self):
        res = self.controller.create({'name': 'test_category'})
        assert res['name'] == 'test_category'

    def test_get_all_categories(self):
        res = self.controller.get_all()
        assert res == []

    def test_update_category(self):
        category = self.controller.create({'name': 'test_category'})
        res = self.controller.update(category['id'], {'name': 'new_test_category'})
        assert res['name'] == 'new_test_category'
        assert res['id'] == category['id']

    def test_delete_category(self):
        category = self.controller.create({'name': 'test_category'})
        res = self.controller.delete(category['id'])
        assert res == True