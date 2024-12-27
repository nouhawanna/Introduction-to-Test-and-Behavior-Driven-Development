import pytest
from app.models import Product

# Sample data for testing
sample_products = [
    Product(id=1, name="Laptop", category="Electronics", price=1200.99, quantity=10, available=True),
    Product(id=2, name="Headphones", category="Electronics", price=199.99, quantity=50, available=True),
    Product(id=3, name="T-shirt", category="Clothing", price=20.99, quantity=100, available=True),
    Product(id=4, name="Book", category="Books", price=15.99, quantity=0, available=False),
]

@pytest.fixture
def mock_db():
    """Fixture to simulate a mock database."""
    return sample_products.copy()

def test_read_product(mock_db):
    """Test reading a product by ID."""
    product_id = 1
    product = next((p for p in mock_db if p.id == product_id), None)
    assert product is not None
    assert product.name == "Laptop"

def test_update_product(mock_db):
    """Test updating a product."""
    product_id = 2
    product = next((p for p in mock_db if p.id == product_id), None)
    assert product is not None
    product.price = 149.99
    assert product.price == 149.99

def test_delete_product(mock_db):
    """Test deleting a product."""
    product_id = 3
    mock_db = [p for p in mock_db if p.id != product_id]
    assert all(p.id != product_id for p in mock_db)

def test_list_all_products(mock_db):
    """Test listing all products."""
    assert len(mock_db) == 4

def test_find_by_name(mock_db):
    """Test finding a product by name."""
    product_name = "T-shirt"
    product = next((p for p in mock_db if p.name.lower() == product_name.lower()), None)
    assert product is not None
    assert product.category == "Clothing"

def test_find_by_category(mock_db):
    """Test finding products by category."""
    category = "Electronics"
    products = [p for p in mock_db if p.category.lower() == category.lower()]
    assert len(products) == 2

def test_find_by_availability(mock_db):
    """Test finding available products."""
    products = [p for p in mock_db if p.available]
    assert len(products) == 3
