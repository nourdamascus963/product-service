from behave import given

@given("the following products exist")
def step_impl(context):
    context.products = [
        {"id": 1, "name": "Hat", "category": "Clothing", "available": True},
        {"id": 2, "name": "Shoes", "category": "Clothing", "available": True},
        {"id": 3, "name": "Big Mac", "category": "Food", "available": False}
    ]
