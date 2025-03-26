Feature: Cart tests

  Scenario: User can check if cart is empty
    Given Open target main page
    When Click on cart
    Then Verify cart is empty

  Scenario: User can add any product in cart
    Given Open target main page
    When Search for plates
    When Click add to cart btn
    When Confirm Add to Cart button from side navigation
    When Open Cart
    Then Verify Cart has 1 item