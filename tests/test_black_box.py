import math
import json
import requests
from parameterized import parameterized

def test_circle_area_valid_positive_radius():
    """Test the /circle-area endpoint with a valid positive radius"""
    response = requests.get("http://localhost:5000/circle-area?radius=5")
    assert response.status_code == 200
    result = json.loads(response.content)
    assert "area" in result
    assert round(result["area"], 4) == round(math.pi * (5**2), 4)

@parameterized.expand([
        (0, "Radius must be a positive number."),
        (-20, "Radius must be a positive number.")
    ])
def test_circle_area_zero_or_negative_radius(radius, expected):
    """Test the /circle-area endpoint with a zero or negative radius"""
    response = requests.get("http://localhost:5000/circle-area?radius={}".format(radius))
    assert response.status_code == 400
    result = json.loads(response.content)
    assert "error" in result
    assert result["error"] == expected

def test_circle_area_negative_radius():
    """Test the /circle-area endpoint with a negative radius"""
    response = requests.get("http://localhost:5000/circle-area?radius=-5")
    assert response.status_code == 400
    result = json.loads(response.content)
    assert "error" in result
    assert result["error"] == "Radius must be a positive number."

def test_circle_area_nonnumeric_radius():
    """Test the /circle-area endpoint with non-numeric input"""
    response = requests.get("http://localhost:5000/circle-area?radius=hello")
    assert response.status_code == 400
    result = json.loads(response.content)
    assert "error" in result
    assert result["error"] == "Radius must be a positive number."

def test_circle_area_large_radius():
    """Test the /circle-area endpoint with very large input"""
    response = requests.get("http://localhost:5000/circle-area?radius=1e6")
    assert response.status_code == 200
    result = json.loads(response.content)
    assert "area" in result
    assert round(result["area"], 4) == round(math.pi * (1e6**2), 4)

def test_circle_area_rounding():
    """Test the /circle-area endpoint for correct rounding of small numbers"""
    response = requests.get("http://localhost:5000/circle-area?radius=0.1")
    assert response.status_code == 200
    result = json.loads(response.content)
    assert "area" in result
    assert round(result["area"], 4) == round(math.pi * (0.1**2), 4)