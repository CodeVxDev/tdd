from flask import Flask
import json
import unittest
from src import main
from parameterized import parameterized

class CircleAreaTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = main.app.test_client()

    @parameterized.expand([
        (0, 0),
        ("abc", "Invalid Radius"),
        (-20, 1256.6370614359173)
    ])    
    def test_circle_area(self, radius, expected):
        # Send a GET request to the endpoint
        response = self.client.get('/circle-area?radius={}'.format(radius))

        # Parse the JSON response
        data = json.loads(response.data)

        # Check that the correct area is returned
        assert data['area'] == expected

if __name__ == '__main__':
    unittest.main()