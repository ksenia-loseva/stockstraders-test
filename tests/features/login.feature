@login
  Feature: Login Page
    Scenario: Successful Login
      Given I am a registered user

      When I go to login page
      And I enter email
      And I enter password
      And I click Continue button

      Then trading interface should load