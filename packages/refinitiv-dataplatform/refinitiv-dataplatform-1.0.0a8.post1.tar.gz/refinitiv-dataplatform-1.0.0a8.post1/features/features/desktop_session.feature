Feature: Desktop Session
  As a Citizen developer
  I want to be able to connect to Eikon Proxy using elektron-api-library
  so that I can have configured session to retrieve data from Eikon Proxy

  @desktop_session
  Scenario: Verify that Desktop Session is opened
    Given I have an Eikon application is running
    When I input the correct application key and port number
    And I open session
    Then I receive a notification that session is opened

  @desktop_session
  Scenario: Verify that Desktop Session is not opened and error notification received using incorrect application key
    Given I have an Eikon application is running
    When I input the incorrect application key
    And I open session
    Then I receive response with status code "400"
    And I receive an error notification: "App key is incorrect"

  @desktop_session
  Scenario: Verify that Desktop Session is not opened and error notification received if Eikon is not running
    Given I have an Eikon application is not running
    When I open session
    Then I receive an error notification about Api Proxy port: "Eikon is not running", network error