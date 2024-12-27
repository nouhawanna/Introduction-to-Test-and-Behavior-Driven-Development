from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory "database" for demonstration
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1200.99, "quantity": 10, "available": True},
    {"id": 2, "name": "Headphones", "category": "Electronics", "price": 199.99, "quantity": 50, "available": True},
    {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 20.99, "quantity": 100, "available": True},
    {"id": 4, "name": "Book", "category": "Books", "price": 15.99, "quantity": 0, "available": False},
]

@app.route('/products', methods=['GET'])
def list_products():
    """List all products or filter by query parameters."""
    name = request.args.get('name')
    category = request.args.get('category')
    available = request.args.get('available')

    filtered_products = products
    if name:
        filtered_products = [p for p in filtered_products if p['name'].lower() == name.lower()]
    if category:
        filtered_products = [p for p in filtered_products if p['category'].lower() == category.lower()]
    if available:
        available_bool = available.lower() == 'true'
        filtered_products = [p for p in filtered_products if p['available'] == available_bool]

    return jsonify(filtered_products), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def read_product(product_id):
    """Read a specific product by ID."""
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        abort(404, description="Product not found")
    return jsonify(product), 200

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update a specific product by ID."""
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        abort(404, description="Product not found")
    
    data = request.get_json()
    for key in ['name', 'category', 'price', 'quantity', 'available']:
        if key in data:
            product[key] = data[key]
    
    return jsonify(product), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a specific product by ID."""
    global products
    products = [p for p in products if p['id'] != product_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
