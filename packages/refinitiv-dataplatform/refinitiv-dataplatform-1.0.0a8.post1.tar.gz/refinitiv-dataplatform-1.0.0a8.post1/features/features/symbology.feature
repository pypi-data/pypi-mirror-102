Feature: Symbology - Convert Symbols

  Background: User has username, password and app_key
    Given platform session created

  @symbology
  Scenario: Convert symbol to all symbol types
    Given platform session opens
    When User performs convert symbol "MSFT.O" from "RIC" type to "All"
    Then data is retrieved

  @symbology
  Scenario: Try convert symbol with closed session
    Given platform session opens
    And platform session closed
    When User performs convert symbol "MSFT.O"
    Then error is raised with message "Session is not opened. Can't send any request"

  @symbology
  Scenario: Convert one symbols from RIC type to one specific symbol type
    Given platform session opens
    When User performs convert symbol "AAPL.O" from "RIC" type to "LipperID"
    Then data is retrieved

  @symbology
  Scenario: Try convert incorrect symbol
    Given platform session opens
    When User performs convert symbol "ABCDEFG.123"
    Then empty data is retrieved

  @symbology
  Scenario: Convert many symbols from ISIN type to many specific symbol types
    Given platform session opens
    When User performs convert symbol "US02079K1079" from "ISIN" type to "RIC,OAPermID"
    Then data is retrieved

  @symbology
  Scenario: Try convert symbol from ISIN type to incorrect symbol type
    Given platform session opens
    When User performs convert symbol "US02079K1079" from "ISIN" type to "Inv123!"
    Then data is retrieved
