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
@app.route("/products", methods=["GET"])
def list_all_products():
    """List all products"""
    return jsonify(products), 200


@app.route("/products/name/<string:name>", methods=["GET"])
def list_by_name(name):
    """List products by name"""
    result = [p for p in products if p["name"].lower() == name.lower()]
    return jsonify(result), 200


@app.route("/products/category/<string:category>", methods=["GET"])
def list_by_category(category):
    """List products by category"""
    result = [p for p in products if p["category"].lower() == category.lower()]
    return jsonify(result), 200


@app.route("/products/available/<string:available>", methods=["GET"])
def list_by_availability(available):
    """List products by availability"""
    is_available = available.lower() == "true"
    result = [p for p in products if p.get("available", True) == is_available]
    return jsonify(result), 200
