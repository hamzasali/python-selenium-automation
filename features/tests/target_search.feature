Feature: Target search test cases

  Scenario: User can search for a product on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search result


  Scenario: User can check if cart is empty
    Given Open target main page
    When Click on cart
    Then Verify cart is empty


  Scenario: User can sign in
    Given Open target main page
    When Click Sign in
    When Click Sign in from menu
    Then Verify Sign in form opened