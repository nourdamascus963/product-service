Feature: Product Service

  Scenario: Read a product
    Given the product service is running
    When I request a product by id
    Then the product details are returned

  Scenario: Update a product
    Given the product service is running
    When I update a product by id
    Then the updated product is returned

  Scenario: Delete a product
    Given the product service is running
    When I delete a product by id
    Then the product is removed

  Scenario: List all products
    Given the product service is running
    When I request all products
    Then a list of products is returned

  Scenario: Search products by name
    Given the product service is running
    When I search products by name
    Then matching products are returned

  Scenario: Search products by category
    Given the product service is running
    When I search products by category
    Then matching products are returned

  Scenario: Search products by availability
    Given the product service is running
    When I search products by availability
    Then matching products are returned
