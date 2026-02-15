"""
Routes for Product Service
"""

from flask import Flask, jsonify

app = Flask(__name__)

# Mock data
products = [
    {"id": 1, "name": "Hat", "category": "Clothing"},
    {"id": 2, "name": "Shoes", "category": "Clothing"},
    {"id": 3, "name": "Big Mac", "category": "Food"}
]

@app.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    """READ a product by ID"""
    for product in products:
        if product["id"] == product_id:
            return jsonify(product), 200
    return jsonify({"message": "Product not found"}), 404
