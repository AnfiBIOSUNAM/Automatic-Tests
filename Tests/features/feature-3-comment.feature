Feature: Add a comment
    Scenario: Comment a product
    Given We are in the website
    When Go to my shopping
    When Select the last element bought
    when Comment the product
    Then Check if the product is commented