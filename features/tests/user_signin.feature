Feature: User sign in tests

  Scenario: User can access sign in
    Given Open target main page
    When Click Sign in
    When Click Sign in from menu
    Then Verify Sign in form opened

#  Scenario: User can open and close Terms and Conditions from sign in page
#    Given Open sign in page
#    And Store original window
#    When Click on Target terms and conditions link
#    And Switch to new window
#    Then Verify Terms and Conditions page is opened
#    And Close current page
#    And Return to original window

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    When Click Sign in
    And Click Sign in from menu
    When Click on Target terms and conditions link
    Then Verify Terms and Conditions page is opened