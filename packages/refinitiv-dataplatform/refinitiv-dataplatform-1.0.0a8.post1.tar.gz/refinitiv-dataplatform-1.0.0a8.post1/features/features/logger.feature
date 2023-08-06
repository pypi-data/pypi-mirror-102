Feature: Logger

  Background: Enabled log
    Given I enabled to log in the file and set logs.transports.file.enabled to true

  Scenario: Total count of all rotated log files
    Given I use a logger in the Library
    And Default total count of all rotated log files is to 10
    When I set logs.transports.file.maxFiles to 4
    Then Total count of all rotated log files will be no more than 4

  Scenario: Logs are being written by the logger contain the module name
    Given I use a logger in the Library
    When I create new logger using a module name
    Then Logs are being written by this logger contain this module name (i.e. [session:desktop])
    And Timestamp in ISO format ([2020-09-16T07:45:40.632Z]) is used for each log message
    And Each log message contains log LEVEL name (i.e. [INFO])
    And Each log message contains thread ID (i.e. [20566])

  Scenario Outline: All levels below or equal VALUE are logged
    Given available log levels
      | string value | integer value |
      | trace        | 0             |
      | debug        | 1             |
      | info         | 2             |
      | warn         | 3             |
      | error        | 4             |
    And I use a logger in the Library
    When I set logs.level to <value>
    Then All levels higher or equal <value> are logged
    # (i.e. if set 'info'(2) then 'info'(2), 'warn'(3) and 'error'(4) levels will be logged)
    Examples: String values
      | value |
      | trace |
      | debug |
      | info  |
      | warn  |
      | error |
    Examples: Integer values
      | value |
      | 0     |
      | 1     |
      | 2     |
      | 3     |
      | 4     |

  Scenario: Logs are not written at all
    Given I use a logger in the Library
    When I set logs.level to silent
    Then Logs are not written at all

  Scenario: Default log level is 'info', by default logs are written to the console and to file
    Given I use a logger in the Library
    When I use any of logger method to write logs
    Then Logs are written to the console, to the file, level higher or equal 'info'

  Scenario: Date, time, and process ID are added to the log file name
    Given I get a logger in the Library
    When logs are logged to a file
    Then Date, time, and process ID are added to the log file name defined in 'logs.transports.file.name' field default to 'refinitiv-data-platform-lib.log'
#  (i.e. 20200916-1720-20566-refinitiv-data-platform-lib)
    And After rotating the file - the sequence number is added to the file name
#  (i.e. 20200916-1720-1-20566-refinitiv-data-platform-lib)

  Scenario Outline: Single log file size
    Given I get a logger in the Library
    And Default single log file size is to 10M
    When I set logs.transports.file.size to <value>
    Then Single log file size will be about <value>
    Examples: File sizes
      | value |
      | 300K  |
      | 300B  |
      | 100M  |

  Scenario: New rotation cycle will be started
    Given I use a logger in the Library
    And Default new rotation cycle will be started to 1d - every midnight
    When I set logs.transports.file.interval to 10s
    Then New rotation cycle will be started at every 10s

  Scenario Outline: Only those logs that matched by filter are written
    Given I use a logger in the Library
    And Default filter is to '*'
    When I set logs.filter to <value>
    Then Only <record> that match the <value> filter are written
    Examples: Filters
      | value                        | record   |
      | *                            | module   |
      | session*,module:b,module:c   | module:b |
      | *,-module:a                  | module:c |
      | module:*,-module:b,-module:c | module:e |
