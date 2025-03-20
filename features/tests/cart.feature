Feature: Cart tests

  Scenario: User can check if cart is empty
    Given Open target main page
    When Click on cart
    Then Verify cart is empty