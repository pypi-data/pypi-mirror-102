Feature: Combined Platform and Deployed Platform sessions
  As a Citizen developer
  I want to be able to connect directly to RDP or local (deployed) real-time enterprise platform (TREP)
  so that I can have one configured session to retrieve data

  @platform_session
  Scenario: Verify that session is opened using valid credentials
    When I open session
    Then I receive a notification that session is opened

  @platform_session
  Scenario: Verify that session is not opened and error notification received using invalid credentials
    When I input 'invalid' RDP credentials
    Then I receive error message "invalid_app_key"

  @platform_session
  Scenario: Verify that token is refreshed automatically
    And I open session
    When My token is going to expire
    Then I receive new valid token with platform session
    And I receive a notification that token refresh success

#  @skip
#  Scenario: Verify that session stops requesting a new token and is closed after failed attempt for token refresh
#    And I input 'valid' RDP credentials
#    And I open session
#    When My token is going to expire
#    And My attempt to refresh token with platform session is failed
#    Then I receive a notification that token refresh failed
#    And Session stops requesting a new token and is closed
#    And I receive a notification that session is closed
#
#  @skip
#  Scenario: Verify that session using valid credentials and valid host
#    Given I want to set up 'platform' session
#    When I input 'valid' RDP credentials
#    And I input the 'valid' host value
#    And I open session
#    Then I receive a notification that session is opened
#
#  @skip
#  Scenario: Verify that I receive an error notification when a TREP host is invalid
#    Given I want to set up 'platform' session
#    When I input 'valid' RDP credentials
#    And I input the 'invalid' host value
#    And I open session
#    Then I receive a notification that 'StreamDisconnected'
#
#  @skip
#  Scenario: Verify that I receive an error notification when a TREP host port is invalid
#    Given I have a valid RDP credentials and want to set up session
#    When I input my appKey, username and password
#    And I input the invalid host port value
#    And I open session PLATFORM_SESSION_WITH_INVALID_HOST_PORT
#    Then I receive a notification that REFUSED_CONNECTION
#
#  @skip
#  Scenario: Verify that I receive an error notification when I try open session and don't pass parameters
#    Given I have a valid RDP credentials and want to set up session
#    When I input my appKey and don't pass parameters
#    And I open session PLATFORM_SESSION_WITHOUT_PARAMETERS
#    Then I receive a notification that I_NEED_TO_PROVIDE_CREDENTIALS
#
#  @skip
#  Scenario: Verify that I receive an error notification when a appKey is invalid
#    Given I have a valid RDP credentials and want to set up session
#    When I input invalid appKey
#    And I open session PLATFORM_SESSION_WITH_INVALID_APPKEY
#    Then I receive response with STATUS_CODE_401
#    Then I receive a notification that INVALID_APPLICATION_CREDENTIAL
#
#  @skip
#  Scenario: Verify that I can use content objects with TREP host
#    Given I have opened session with TREP host and RDP credentials
#    When I try to USE_CONTENT_OBJECT_WITH_PLATFORM_SESSION_AND_HOST
#    Then I receive event: SUCCESS_RESULT_EVENT
#    And I receive content object data with HISTORICAL_PRICING_EVENTS_DATA
#
#  @skip
#  Scenario: Verify that I can use streaming with TREP host
#    Given I have opened session with TREP host and RDP credentials
#    When I try to USE_STREAMING_WITH_PLATFORM_SESSION_AND_HOST
#    Then I start receiving STREAMING_DATA_WITH_SPECIFIC_NAME
#
#  @skip
#  Scenario: Verify that I can use endpoints with TREP host
#    Given I have opened session with TREP host and RDP credentials
#    When I try to USE_ENDPOINT_WITH_PLATFORM_SESSION_AND_HOST
#    Then I receive response with STATUS_CODE_200
#
#  @skip
#  Scenario: Verify that I can use endpoints when I pass only TREP host and dont pass credentials
#    Given I want to set up session with TREP host and don't pass RDP credentials
#    When I try to USE_ENDPOINT_WITH_HOST_AND_WITHOUT_CREDENTIALS
#    Then I receive a notification that PLATFORM_SESSION_WITHOUT_RDP_CREDENTIALS_ONLY_SUPPORTS_STREAMING_CONNECTION
