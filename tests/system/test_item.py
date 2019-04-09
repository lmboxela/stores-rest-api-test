from models.item import ItemModel
from models.store import StoreModel
from models.user import UserModel
from tests.base_test import BaseTest
import json


class ItemTest(BaseTest):
    """def setUp(self):
        super(ItemTest, self).setUp()
        with self.app() as client:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                auth_request = client.post('/auth',
                                           data=json.dumps({'username': 'test', 'password': '1234'}),
                                           headers={'Content_Type': 'application/json'})
                auth_token = json.loads(auth_request.data)['access_token']
                self.access_token = f'JWT {auth_token}'"""

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('/item/test')
                self.assertEqual(resp.status_code, 401)

    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                headers = {'Content-Type': 'application/json'}
                auth_request = client.post('/auth',
                                           data=json.dumps({'username': 'test', 'password': '1234'}),
                                           content_type='application/json')
                print(auth_request)
                auth_token = json.loads(auth_request.data)['access_token']
                header = {'Authorization': f'JWT {auth_token}'}
                resp = client.get('/item/test', headers=header)
                self.assertEqual(resp.status_code, 404)

    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                pass

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():
                pass

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():
                pass

    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                pass

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                pass

    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():
                pass

    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                pass
