Feature: Manage Products
  As a user
  I want to manage products
  So that I can retrieve, update, delete, and search products easily

  Background:
    Given the following products are loaded into the database
      | id | name       | category    | price  | quantity | available |
      | 1  | Laptop     | Electronics | 1200.99 | 10      | true      |
      | 2  | Headphones | Electronics | 199.99  | 50      | true      |
      | 3  | T-shirt    | Clothing    | 20.99   | 100     | true      |
      | 4  | Book       | Books       | 15.99   | 0       | false     |

  Scenario: List all products
    When I send a GET request to "/products"
    Then the response status code should be 200
    And the response should contain 4 products

  Scenario: Read a product by ID
    When I send a GET request to "/products/1"
    Then the response status code should be 200
    And the response should contain the product "Laptop"

  Scenario: Update a product by ID
    Given the product with ID 1 has the following updates
      | name     | price  |
      | Ultrabook | 1500.99 |
    When I send a PUT request to "/products/1" with the updated data
    Then the response status code should be 200
    And the response should contain the updated product "Ultrabook"

  Scenario: Delete a product by ID
    When I send a DELETE request to "/products/3"
    Then the response status code should be 204
    And the product with ID 3 should no longer exist

  Scenario: Search products by name
    When I send a GET request to "/products?name=Headphones"
    Then the response status code should be 200
    And the response should contain 1 product
    And the product name should be "Headphones"

  Scenario: Search products by category
    When I send a GET request to "/products?category=Electronics"
    Then the response status code should be 200
    And the response should contain 2 products
    And the products should include "Laptop" and "Headphones"

  Scenario: Search products by availability
    When I send a GET request to "/products?available=true"
    Then the response status code should be 200
    And the response should contain 3 products
    And the products should include "Laptop", "Headphones", and "T-shirt"
