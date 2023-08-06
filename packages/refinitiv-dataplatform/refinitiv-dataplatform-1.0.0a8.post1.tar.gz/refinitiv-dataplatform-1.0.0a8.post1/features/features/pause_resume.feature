Feature: Pause/Resume for ItemStream, StreamingPrices, StreamingChain

  Background: User has username, password and app_key
    Given platform session created

  Scenario Outline: Set stream to pause
    Given platform session opens
    And <stream_name> created
    When User set stream to pause
    Then stream paused
    And I close session

    Examples:
      | stream_name     |
      | ItemStream      |
      | StreamingPrices |
      | StreamingChain  |

  Scenario Outline: Set stream to pause and then resume
    Given platform session opens
    And <stream_name> created
    And stream paused
    When User resume stream
    Then stream resumed
    And I close session

    Examples:
      | stream_name     |
      | ItemStream      |
      | StreamingPrices |
      | StreamingChain  |