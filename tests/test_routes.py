import pytest
from app import create_app
from app.models import Product

# Sample data for tests
sample_products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1200.99, "quantity": 10, "available": True},
    {"id": 2, "name": "Headphones", "category": "Electronics", "price": 199.99, "quantity": 50, "available": True},
    {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 20.99, "quantity": 100, "available": True},
    {"id": 4, "name": "Book", "category": "Books", "price": 15.99, "quantity": 0, "available": False},
]

@pytest.fixture
def client():
    """Fixture to set up the Flask test client."""
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_read_product(client):
    """Test the GET /products/<id> route."""
    response = client.get("/products/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Laptop"

def test_update_product(client):
    """Test the PUT /products/<id> route."""
    updated_data = {"name": "Gaming Laptop", "price": 1500.99}
    response = client.put("/products/1", json=updated_data)
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "Gaming Laptop"
    assert data["price"] == 1500.99

def test_delete_product(client):
    """Test the DELETE /products/<id> route."""
    response = client.delete("/products/3")
    assert response.status_code == 204
    response = client.get("/products/3")
    assert response.status_code == 404

def test_list_all_products(client):
    """Test the GET /products route."""
    response = client.get("/products")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == len(sample_products)

def test_list_by_name(client):
    """Test the GET /products?name=<name> route."""
    response = client.get("/products?name=T-shirt")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["name"] == "T-shirt"

def test_list_by_category(client):
    """Test the GET /products?category=<category> route."""
    response = client.get("/products?category=Electronics")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2

def test_list_by_availability(client):
    """Test the GET /products?available=true route."""
    response = client.get("/products?available=true")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 3
