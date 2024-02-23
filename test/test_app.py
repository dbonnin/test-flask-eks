import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_data(self):
        response = self.app.get('/api/data')
        self.assertEqual(response.status_code, 200)
        # Add additional assertions to validate the response data

if __name__ == '__main__':
    unittest.main()
