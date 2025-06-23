import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Back-End GitHub User Finder', response.data)

    def test_user_search(self):
        response = self.app.get('/search?username=octocat')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User: octocat', response.data)

    def test_invalid_user(self):
        response = self.app.get('/search?username=invaliduser')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'User not found', response.data)

if __name__ == '__main__':
    unittest.main()