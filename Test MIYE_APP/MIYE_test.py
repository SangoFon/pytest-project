# import pytest

from app import app
import unittest
# import pytest
# @pytest.fixture(scope="module")
# def context():
#     data={'db': 'db', 'User': 'User','Room':'Room'}
#     return data
# def test_context(context):
#     assert "User", 'User' in data
# @pytest.fixture()
# # @login.user_loader
# def load_user(id):
#     return get(int(id))
# def test_load_user(load_user):
#     assert get(int(1))==1
class FlaskTestCase(unittest.TestCase):
    print("test flask setup")
    def test_index(self):
        tester =app.test_client(self)
        response =tester.get('/login',content_type='html/text')
        self.assertEqual(response.status_code,200)

    print("test login page loads correctly")
    def test_login_page_loads(self):
        tester =app.test_client(self)
        response =tester.get('/login',content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

        print("test access")
    def test_access(self):
        tester =app.test_client(self)
        response =tester.get(
        '/login',
        data=dict(username="admin",password="wenxing"),
        follow_redirects=True
        )
        self.assertTrue(b'You have gained access!', response.data)
        print("test logout")

    def test_logout(self):
        tester =app.test_client(self)
        tester.post(
        '/login',
        data=dict(username="admin",password="wenxing"),
        follow_redirects=True
        )
        response = tester.get('/logout',follow_redirects=True)
        self.assertTrue(b'You have lost access!', response.data)

if __name__=='__main__':
    unittest.main()
