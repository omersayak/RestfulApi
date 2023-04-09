from app.controllers.user_controller import UserController

class TestUser:
    def setup_method(self):
        self.controller = UserController()

    def test_create_user(self):
        res = self.controller.create({'name': 'Test User', 'email': 'user@test.com', 'password': 'password123'})
        assert res['name'] == 'Test User'
        assert res['email'] == 'user@test.com'

    def test_get_all_users(self):
        res = self.controller.get_all()
        assert res == []

    def test_update_user(self):
        user = self.controller.create({'name': 'Test User', 'email': 'user@test.com', 'password': 'password123'})
        res = self.controller.update(user['id'], {'name': 'New Test User', 'email': 'newuser@test.com'})
        assert res['name'] == 'New Test User'
        assert res['email'] == 'newuser@test.com'
        assert res['id'] == user['id']

    def test_delete_user(self):
        user = self.controller.create({'name': 'Test User', 'email': 'user@test.com', 'password': 'password123'})
        res = self.controller.delete(user['id'])
        assert res == True