Feature: Target search test cases

#
#  Scenario: User can search for a product on Target
#    Given Open target main page
#    When Search for tea
#    Then Verify correct search result shown for tea
#
#
#  Scenario: User can search for a product on Target
#    Given Open target main page
#    When Search for iPhone
#    Then Verify correct search result shown for iPhone
#
#
#  Scenario: User can search for a product on Target
#    Given Open target main page
#    When Search for shoes
#    Then Verify correct search result shown for shoes


  Scenario: User can sign in
    Given Open target main page
    When Click Sign in
    When Click Sign in from menu
    Then Verify Sign in form opened

  Scenario Outline: User can search for a product on Target
    Given Open target main page
    When Search for <search_word>
    Then Verify correct search result shown for <expected_result>
    Examples:
      | search_word | expected_result |
      | tea         | tea             |
      | iPhone      | iPhone          |
      | shoes       | shoes           |


  Scenario: User can add any product in cart
    Given Open target main page
    When Search for mugs
    When Click add to cart btn
    And Store product name
    When Confirm Add to Cart button from side navigation
    When Open Cart
    Then Verify Cart has 1 item
    Then Verify cart has correct product


  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image