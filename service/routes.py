"""
Product Service Routes
"""

from flask import Flask, jsonify

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
