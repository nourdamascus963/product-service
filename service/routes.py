"""
Product Service Routes
"""

from flask import Flask, jsonify,request

app = Flask(__name__)

# Sample data
products = [
    {"id": 1, "name": "Hat", "category": "Clothing"},
    {"id": 2, "name": "Shoes", "category": "Clothing"},
    {"id": 3, "name": "Big Mac", "category": "Food"}
]

@app.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    """Read a product by ID"""
    for product in products:
        if product["id"] == product_id:
            return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """Update a product by ID"""
    data = request.get_json()
    for product in products:
        if product["id"] == product_id:
            product.update(data)
            return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404
    
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Delete a product by ID"""
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return jsonify({"message": "Product has been Deleted!"}), 200
    return jsonify({"error": "Product not found"}), 404
