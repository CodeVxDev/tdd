from flask import Flask
import json
import unittest
from src import main
from parameterized import parameterized

class CircleAreaTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = main.app.test_client()

    def test_circle_area(self, radius, expected):
        # Send a GET request to the endpoint
        response = self.client.get('/circle-area?radius={}'.format(25))

        # Parse the JSON response
        data = json.loads(response.data)

        # Check that the correct area is returned
        assert data['area'] == 1963.4954084936207
    
    @parameterized.expand([
        (0, "Radius must be a positive number."),
        ("abc", "Radius must be a positive number."),
        (-20, "Radius must be a positive number.")
    ])    
    def test_circle_area(self, radius, expected):
        # Send a GET request to the endpoint
        response = self.client.get('/circle-area?radius={}'.format(radius))

        # Parse the JSON response
        data = json.loads(response.data)

        # Check that the correct area is returned
        assert data['error'] == expected

if __name__ == '__main__':
    unittest.main()