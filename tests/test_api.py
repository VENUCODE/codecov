import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestAddEndpoint:
    """Test cases for the /add endpoint."""
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        response = client.post("/add", json={"a": 10, "b": 5})
        assert response.status_code == 200
        assert response.json() == {"result": 15}
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        response = client.post("/add", json={"a": -10, "b": -5})
        assert response.status_code == 200
        assert response.json() == {"result": -15}
    
    def test_add_mixed_numbers(self):
        """Test addition with mixed positive and negative numbers."""
        response = client.post("/add", json={"a": 10, "b": -5})
        assert response.status_code == 200
        assert response.json() == {"result": 5}
    
    def test_add_decimal_numbers(self):
        """Test addition with decimal numbers."""
        response = client.post("/add", json={"a": 10.5, "b": 5.2})
        assert response.status_code == 200
        assert response.json() == {"result": 15.7}
    
    def test_add_zero(self):
        """Test addition with zero."""
        response = client.post("/add", json={"a": 10, "b": 0})
        assert response.status_code == 200
        assert response.json() == {"result": 10}
    
    def test_add_missing_field(self):
        """Test addition with missing field."""
        response = client.post("/add", json={"a": 10})
        assert response.status_code == 422
    
    def test_add_invalid_type(self):
        """Test addition with invalid type."""
        response = client.post("/add", json={"a": "invalid", "b": 5})
        assert response.status_code == 422


class TestSubtractEndpoint:
    """Test cases for the /subtract endpoint."""
    
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        response = client.post("/subtract", json={"a": 10, "b": 5})
        assert response.status_code == 200
        assert response.json() == {"result": 5}
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        response = client.post("/subtract", json={"a": -10, "b": -5})
        assert response.status_code == 200
        assert response.json() == {"result": -5}
    
    def test_subtract_mixed_numbers(self):
        """Test subtraction with mixed positive and negative numbers."""
        response = client.post("/subtract", json={"a": 10, "b": -5})
        assert response.status_code == 200
        assert response.json() == {"result": 15}
    
    def test_subtract_decimal_numbers(self):
        """Test subtraction with decimal numbers."""
        response = client.post("/subtract", json={"a": 10.5, "b": 5.2})
        assert response.status_code == 200
        assert abs(response.json()["result"] - 5.3) < 0.0001
    
    def test_subtract_zero(self):
        """Test subtraction with zero."""
        response = client.post("/subtract", json={"a": 10, "b": 0})
        assert response.status_code == 200
        assert response.json() == {"result": 10}
    
    def test_subtract_missing_field(self):
        """Test subtraction with missing field."""
        response = client.post("/subtract", json={"a": 10})
        assert response.status_code == 422
    
    def test_subtract_invalid_type(self):
        """Test subtraction with invalid type."""
        response = client.post("/subtract", json={"a": "invalid", "b": 5})
        assert response.status_code == 422


class TestMultiplyEndpoint:
    """Test cases for the /multiply endpoint."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        response = client.post("/multiply", json={"a": 10, "b": 5})
        assert response.status_code == 200
        assert response.json() == {"result": 50}
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        response = client.post("/multiply", json={"a": -10, "b": -5})
        assert response.status_code == 200
        assert response.json() == {"result": 50}
    
    def test_multiply_mixed_numbers(self):
        """Test multiplication with mixed positive and negative numbers."""
        response = client.post("/multiply", json={"a": 10, "b": -5})
        assert response.status_code == 200
        assert response.json() == {"result": -50}
    
    def test_multiply_decimal_numbers(self):
        """Test multiplication with decimal numbers."""
        response = client.post("/multiply", json={"a": 10.5, "b": 5.2})
        assert response.status_code == 200
        assert abs(response.json()["result"] - 54.6) < 0.0001
    
    def test_multiply_zero(self):
        """Test multiplication with zero."""
        response = client.post("/multiply", json={"a": 10, "b": 0})
        assert response.status_code == 200
        assert response.json() == {"result": 0}
    
    def test_multiply_missing_field(self):
        """Test multiplication with missing field."""
        response = client.post("/multiply", json={"a": 10})
        assert response.status_code == 422
    
    def test_multiply_invalid_type(self):
        """Test multiplication with invalid type."""
        response = client.post("/multiply", json={"a": "invalid", "b": 5})
        assert response.status_code == 422

