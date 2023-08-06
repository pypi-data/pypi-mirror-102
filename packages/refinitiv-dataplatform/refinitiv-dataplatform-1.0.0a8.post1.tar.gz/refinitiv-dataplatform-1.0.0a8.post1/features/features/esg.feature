Feature: ESG - environment, social, government

  Background: User has username, password and app_key
    Given platform session created

  @esg
  Scenario: Get list of instruments in the ESG Universe
    Given platform session opens
    When User performs get list of instruments
    Then data is retrieved

  @esg
  Scenario: Get view of ESG content using correct RIC code
    Given platform session opens
    And code is "AAPL.O"
    When User performs get basic view
    Then data is retrieved

  @esg
  Scenario: Get view of ESG content using incorrect RIC code
    Given platform session opens
    And code is "AA11111PL.O"
    When User performs get basic view
    Then error is received

  @esg
  Scenario: Get view of ESG content without passing code
    Given platform session opens
    When User performs get basic view
    Then error is raised with message "Universe was not requested."

  @esg
  Scenario: Get view of ESG content using correct range
    Given platform session opens
    And code is "AAPL.O"
    And range is "-1":"0"
    When User performs get scores-standard view
    Then data is retrieved

  @esg
  Scenario: Get view of ESG content using invalid range
    Given platform session opens
    And code is "AAPL.O"
    And range is "-3":"-1"
    When User performs get measures-standard view
    Then error is received

  @esg
  Scenario: Get view of ESG content not using range
    Given platform session opens
    And code is "AAPL.O"
    When User performs get measures-full view
    Then data is retrieved

  @esg
  Scenario: Get view of ESG content in callback
    Given platform session opens
    And code is "AAPL.O"
    When User performs get scores-full view in callback
    Then data is retrieved



