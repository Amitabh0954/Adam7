import unittest
from app.app import app

class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_example(self):
        response = self.app.get('/example')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'This is an example endpoint'})

if __name__ == '__main__':
    unittest.main()