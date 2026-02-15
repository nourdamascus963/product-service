Feature: Product Service API

  Scenario: List all products
    Given the product service is running
    When I request all products
    Then I should receive a list of products

  Scenario: Find product by name
    Given the product service is running
    When I search for a product by name "Hat"
    Then I should receive matching products

  Scenario: Find product by category
    Given the product service is running
    When I search for products in category "Clothing"
    Then I should receive products in that category
Scenario: List products by category
  Given the product service is running
  When I search for products in category "Clothing"
  Then I should receive products in that category
Scenario: List products by availability
  Given the product service is running
  When I search for products with availability "true"
  Then I should receive only available products
