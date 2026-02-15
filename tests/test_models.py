"""
Test cases for Product model
"""

class Product:
    def __init__(self, name, category):
        self.name = name
        self.category = category


def test_list_all_products():
    products = [
        Product("Hat", "Clothing"),
        Product("Shoes", "Clothing"),
        Product("Big Mac", "Food")
    ]

    assert len(products) == 3


def test_find_product_by_name():
    products = [
        Product("Hat", "Clothing"),
        Product("Shoes", "Clothing")
    ]

    result = [p for p in products if p.name == "Hat"]
    assert len(result) == 1
    assert result[0].name == "Hat"


def test_find_product_by_category():
    products = [
        Product("Hat", "Clothing"),
        Product("Big Mac", "Food")
    ]

    result = [p for p in products if p.category == "Food"]
    assert len(result) == 1
    assert result[0].name == "Big Mac"
