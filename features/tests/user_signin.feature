Feature: User sign in tests

    Scenario: User can access sign in
    Given Open target main page
    When Click Sign in
    When Click Sign in from menu
    Then Verify Sign in form opened