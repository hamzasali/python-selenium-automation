Feature: Target search test cases

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
#

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
    |search_word  |expected_result  |
    |tea          |tea              |
    |iPhone       |iPhone           |
    |shoes        |shoes            |
