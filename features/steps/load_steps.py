from behave import given
from app import create_app
from app.models import db, Product

# Use the Flask application context for testing
app = create_app()

@given('the following products are loaded into the database')
def step_impl(context):
    """Load products into the database from the Gherkin table."""
    with app.app_context():
        # Clear existing products to start fresh
        db.session.query(Product).delete()
        
        # Parse the table from the Gherkin scenario
        for row in context.table:
            product = Product(
                id=int(row['id']),
                name=row['name'],
                category=row['category'],
                price=float(row['price']),
                quantity=int(row['quantity']),
                available=row['available'].lower() == 'true'
            )
            db.session.add(product)
        
        db.session.commit()
